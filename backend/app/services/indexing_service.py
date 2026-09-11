import os
import json
from typing import List, Dict, Any, Optional
from app.config.config import settings
from app.models.chunk import Chunk
from app.utils.logging import indexing_logger

class IndexingService:
    """
    Manages vector storage and similarity indices.
    Integrates with ChromaDB with a graceful fallback to a local vector store
    to guarantee zero downtime across development setups.
    """
    _instance = None

    def __init__(self):
        self.chroma_dir = settings.VECTOR_DB_DIR
        self.chroma_client = None
        self.collection = None
        self.use_fallback = False
        self.fallback_file = os.path.join(self.chroma_dir, "fallback_vectors.json")
        self._init_chroma()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = IndexingService()
        return cls._instance

    def _init_chroma(self):
        try:
            import chromadb
            from chromadb.config import Settings as ChromaSettings
            os.makedirs(self.chroma_dir, exist_ok=True)
            self.chroma_client = chromadb.PersistentClient(path=self.chroma_dir)
            self.collection = self.chroma_client.get_or_create_collection(
                name="legal_documents",
                metadata={"hnsw:space": "cosine"}
            )
            indexing_logger.info("ChromaDB persistent client initialized successfully.")
        except Exception as e:
            indexing_logger.warning(
                f"ChromaDB persistent client unavailable ({str(e)}). Using local persistent vector store fallback."
            )
            self.use_fallback = True
            os.makedirs(self.chroma_dir, exist_ok=True)

    def add_chunks(self, chunks: List[Chunk], embeddings: List[List[float]]):
        """Indexes a batch of chunks along with their vector embeddings and metadata."""
        if not chunks:
            return

        ids = [chunk.id for chunk in chunks]
        documents = [chunk.text for chunk in chunks]
        metadatas = [
            {
                "document_id": chunk.document_id,
                "document_title": chunk.document_title or "Legal Source",
                "chunk_index": chunk.chunk_index,
                "section_ref": chunk.section_ref or "",
                "page_number": chunk.page_number or 1
            }
            for chunk in chunks
        ]

        if not self.use_fallback and self.collection is not None:
            self.collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas
            )
            indexing_logger.info(f"Upserted {len(chunks)} chunks into ChromaDB collection.")
        else:
            # Local fallback vector store
            store = self._load_fallback_store()
            for i, chunk_id in enumerate(ids):
                store[chunk_id] = {
                    "embedding": embeddings[i],
                    "document": documents[i],
                    "metadata": metadatas[i]
                }
            self._save_fallback_store(store)
            indexing_logger.info(f"Saved {len(chunks)} chunks into local vector store fallback.")

    def delete_document_chunks(self, document_id: str):
        """Removes all chunks associated with a document ID."""
        if not self.use_fallback and self.collection is not None:
            self.collection.delete(where={"document_id": document_id})
            indexing_logger.info(f"Deleted chunks for document {document_id} from ChromaDB.")
        else:
            store = self._load_fallback_store()
            filtered = {k: v for k, v in store.items() if v["metadata"].get("document_id") != document_id}
            self._save_fallback_store(filtered)
            indexing_logger.info(f"Deleted chunks for document {document_id} from fallback store.")

    def get_count(self) -> int:
        """Returns the total number of indexed chunks."""
        if not self.use_fallback and self.collection is not None:
            return self.collection.count()
        else:
            return len(self._load_fallback_store())

    def reset_index(self):
        """Clears all vectors in the collection."""
        if not self.use_fallback and self.chroma_client is not None:
            try:
                self.chroma_client.delete_collection("legal_documents")
                self.collection = self.chroma_client.get_or_create_collection(
                    name="legal_documents",
                    metadata={"hnsw:space": "cosine"}
                )
            except Exception as e:
                indexing_logger.error(f"Error resetting ChromaDB collection: {e}")
        else:
            self._save_fallback_store({})

    def _load_fallback_store(self) -> Dict[str, Any]:
        if os.path.exists(self.fallback_file):
            try:
                with open(self.fallback_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_fallback_store(self, store: Dict[str, Any]):
        with open(self.fallback_file, "w", encoding="utf-8") as f:
            json.dump(store, f)
