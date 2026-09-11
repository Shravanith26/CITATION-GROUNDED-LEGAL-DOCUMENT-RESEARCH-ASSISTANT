from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.citation_schema import ChunkDetailResponse
from app.services.document_service import DocumentService

router = APIRouter(prefix="/api/chunks", tags=["Chunks"])
document_service = DocumentService()

@router.get("/{chunk_id}", response_model=ChunkDetailResponse)
def get_chunk_detail(
    chunk_id: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve a specific chunk's text and source metadata for citation inspection.
    """
    return document_service.get_chunk(chunk_id=chunk_id, db=db)
