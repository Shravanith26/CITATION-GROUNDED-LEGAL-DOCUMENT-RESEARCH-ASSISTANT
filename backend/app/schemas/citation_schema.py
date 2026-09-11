from pydantic import BaseModel
from typing import Optional

class CitationResponse(BaseModel):
    document: str
    section: Optional[str] = None
    snippet: Optional[str] = None
    chunk_id: Optional[str] = None
    confidence_score: Optional[float] = 1.0
    marker_index: Optional[int] = 1

    class Config:
        from_attributes = True

class ChunkDetailResponse(BaseModel):
    id: str
    document_id: str
    document_title: str
    chunk_index: int
    text: str
    section_ref: Optional[str] = None
    page_number: Optional[int] = 1
    similarity_score: Optional[float] = None

    class Config:
        from_attributes = True
