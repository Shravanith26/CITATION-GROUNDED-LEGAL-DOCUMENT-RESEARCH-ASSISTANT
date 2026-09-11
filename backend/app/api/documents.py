import os
from typing import List, Optional
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.document_schema import DocumentResponse, DocumentDetailResponse
from app.services.document_service import DocumentService
from app.utils.file_validation import validate_uploaded_file
from app.config.config import settings

router = APIRouter(prefix="/api/documents", tags=["Documents"])
document_service = DocumentService()

@router.post("", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    title: Optional[str] = Form(None),
    doc_type: Optional[str] = Form("judgment"),
    court_authority: Optional[str] = Form(None),
    citation_ref: Optional[str] = Form(None),
    date: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    """
    Upload and ingest a new legal document (PDF, TXT, MD).
    Triggers extraction, cleaning, chunking, embedding generation, and indexing.
    """
    # Read file content into temporary save path
    contents = await file.read()
    is_valid, err_msg = validate_uploaded_file(file.filename, len(contents))
    if not is_valid:
        raise HTTPException(status_code=400, detail=err_msg)

    save_path = os.path.join(settings.RAW_DOCUMENTS_DIR, file.filename)
    with open(save_path, "wb") as f:
        f.write(contents)

    doc_record = document_service.ingest_document_file(
        file_path=save_path,
        title=title,
        doc_type=doc_type,
        court_authority=court_authority,
        citation_ref=citation_ref,
        date=date,
        db=db
    )
    return doc_record

@router.get("", response_model=List[DocumentResponse])
def list_documents(
    doc_type: Optional[str] = None,
    court: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    List indexed legal documents with optional filtering by type, court, or keyword.
    """
    return document_service.list_documents(doc_type=doc_type, court=court, search=search, db=db)

@router.get("/{doc_id}", response_model=DocumentDetailResponse)
def get_document(doc_id: str, db: Session = Depends(get_db)):
    """
    Retrieve document metadata and its full text.
    """
    return document_service.get_document(doc_id=doc_id, db=db)

@router.delete("/{doc_id}")
def delete_document(doc_id: str, db: Session = Depends(get_db)):
    """
    Remove a document and its chunks from both the metadata DB and vector index.
    """
    document_service.delete_document(doc_id=doc_id, db=db)
    return {"status": "success", "message": f"Document {doc_id} deleted successfully."}
