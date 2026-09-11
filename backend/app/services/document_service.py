import os
import shutil
import uuid
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.config.config import settings
from app.database.models import DocumentModel, ChunkModel
from app.services.extraction_service import ExtractionService
from app.services.preprocessing_service import PreprocessingService
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingServiceImpl
from app.services.indexing_service import IndexingService
from app.utils.logging import ingestion_logger
from app.utils.error_handler import DocumentNotFoundError, ChunkNotFoundError

class DocumentService:
    """
    Coordinates document ingestion, preprocessing, chunking, indexing, and CRUD operations.
    """
    def __init__(self):
        self.extraction_service = ExtractionService()
        self.preprocessing_service = PreprocessingService()
        self.chunking_service = ChunkingService()
        self.embedding_service = EmbeddingServiceImpl()
        self.indexing_service = IndexingService.get_instance()

    def ingest_document_file(
        self,
        file_path: str,
        title: Optional[str] = None,
        doc_type: Optional[str] = "judgment",
        court_authority: Optional[str] = None,
        citation_ref: Optional[str] = None,
        date: Optional[str] = None,
        db: Optional[Session] = None
    ) -> DocumentModel:
        """
        Ingests a document file from disk: extracts, preprocesses, chunks, embeds, and indexes.
        """
        ingestion_logger.info(f"Starting ingestion for file: {file_path}")
        pages = self.extraction_service.extract_from_file(file_path)
        combined_raw = "\n\n".join(p["text"] for p in pages)

        # Parse embedded headers if title not provided
        parsed_meta, cleaned_text = self.preprocessing_service.parse_metadata_headers(combined_raw)
        
        doc_title = title or parsed_meta.get("title") or os.path.splitext(os.path.basename(file_path))[0]
        doc_type = doc_type or parsed_meta.get("doc_type") or "judgment"
        court = court_authority or parsed_meta.get("court_authority")
        citation = citation_ref or parsed_meta.get("citation_ref")
        doc_date = date or parsed_meta.get("date")

        # Save processed text file in processed documents dir
        doc_id = str(uuid.uuid4())
        processed_filename = f"{doc_id}_{os.path.basename(file_path)}.txt"
        processed_path = os.path.join(settings.PROCESSED_DOCUMENTS_DIR, processed_filename)
        with open(processed_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        # Create Database Record
        doc_record = DocumentModel(
            id=doc_id,
            title=doc_title,
            doc_type=doc_type,
            court_authority=court,
            citation_ref=citation,
            date=doc_date,
            source_path=file_path,
            ingestion_status="indexing",
            total_chunks=0
        )
        if db:
            db.add(doc_record)
            db.commit()
            db.refresh(doc_record)

        # Chunk the document
        cleaned_pages = [{"page_number": p["page_number"], "text": self.preprocessing_service.clean_text(p["text"])} for p in pages]
        chunks = self.chunking_service.chunk_document(doc_id, doc_title, cleaned_pages)

        if chunks:
            # Generate Embeddings
            embeddings = self.embedding_service.generate_chunk_embeddings(chunks)

            # Store in Vector Database
            self.indexing_service.add_chunks(chunks, embeddings)

            # Persist Chunk records in relational DB
            if db:
                for chunk in chunks:
                    chunk_record = ChunkModel(
                        id=chunk.id,
                        document_id=doc_id,
                        chunk_index=chunk.chunk_index,
                        text=chunk.text,
                        section_ref=chunk.section_ref,
                        page_number=chunk.page_number,
                        embedding_id=chunk.id
                    )
                    db.add(chunk_record)
                
                doc_record.total_chunks = len(chunks)
                doc_record.ingestion_status = "indexed"
                db.commit()
                db.refresh(doc_record)

        ingestion_logger.info(f"Successfully ingested and indexed '{doc_title}' ({len(chunks)} chunks).")
        return doc_record

    def list_documents(
        self,
        doc_type: Optional[str] = None,
        court: Optional[str] = None,
        search: Optional[str] = None,
        db: Optional[Session] = None
    ) -> List[DocumentModel]:
        """Lists documents with optional filters."""
        if not db:
            return []

        query = db.query(DocumentModel)
        if doc_type:
            query = query.filter(DocumentModel.doc_type == doc_type)
        if court:
            query = query.filter(DocumentModel.court_authority.ilike(f"%{court}%"))
        if search:
            query = query.filter(DocumentModel.title.ilike(f"%{search}%"))

        return query.order_by(DocumentModel.created_at.desc()).all()

    def get_document(self, doc_id: str, db: Session) -> Dict[str, Any]:
        """Retrieves a document's metadata and full text."""
        doc = db.query(DocumentModel).filter(DocumentModel.id == doc_id).first()
        if not doc:
            raise DocumentNotFoundError(doc_id)

        full_text = ""
        chunks = db.query(ChunkModel).filter(ChunkModel.document_id == doc_id).order_by(ChunkModel.chunk_index).all()
        if chunks:
            full_text = "\n\n".join(c.text for c in chunks)
        elif os.path.exists(doc.source_path):
            with open(doc.source_path, "r", encoding="utf-8", errors="replace") as f:
                full_text = f.read()
        else:
            fallback_path = os.path.join(settings.RAW_DOCUMENTS_DIR, os.path.basename(doc.source_path))
            if os.path.exists(fallback_path):
                with open(fallback_path, "r", encoding="utf-8", errors="replace") as f:
                    full_text = f.read()

        return {
            "id": doc.id,
            "title": doc.title,
            "doc_type": doc.doc_type,
            "court_authority": doc.court_authority,
            "citation_ref": doc.citation_ref,
            "date": doc.date,
            "source_path": doc.source_path,
            "ingestion_status": doc.ingestion_status,
            "total_chunks": doc.total_chunks,
            "created_at": doc.created_at,
            "full_text": full_text
        }

    def delete_document(self, doc_id: str, db: Session):
        """Deletes a document from the relational DB and vector store."""
        doc = db.query(DocumentModel).filter(DocumentModel.id == doc_id).first()
        if not doc:
            raise DocumentNotFoundError(doc_id)

        # Delete from vector index
        self.indexing_service.delete_document_chunks(doc_id)

        # Delete from relational DB (cascades to chunks)
        db.delete(doc)
        db.commit()
        ingestion_logger.info(f"Deleted document {doc_id} and its associated chunks.")

    def get_chunk(self, chunk_id: str, db: Session) -> Dict[str, Any]:
        """Retrieves a chunk by ID along with parent document metadata."""
        chunk = db.query(ChunkModel).filter(ChunkModel.id == chunk_id).first()
        if not chunk:
            raise ChunkNotFoundError(chunk_id)

        doc = db.query(DocumentModel).filter(DocumentModel.id == chunk.document_id).first()
        doc_title = doc.title if doc else "Unknown Document"

        return {
            "id": chunk.id,
            "document_id": chunk.document_id,
            "document_title": doc_title,
            "chunk_index": chunk.chunk_index,
            "text": chunk.text,
            "section_ref": chunk.section_ref,
            "page_number": chunk.page_number
        }
