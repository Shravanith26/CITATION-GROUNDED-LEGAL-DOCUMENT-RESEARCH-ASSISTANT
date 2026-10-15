from pydantic import BaseModel, ConfigDict
from typing import Optional

class CitationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    document: str
    section: Optional[str] = None
    snippet: Optional[str] = None
    chunk_id: Optional[str] = None
    confidence_score: Optional[float] = 1.0
    marker_index: Optional[int] = 1
    verification_status: Optional[str] = "Source found"
    verbatim_quote: Optional[str] = None
    quote_found: Optional[bool] = True
    court: Optional[str] = "Supreme Court of India"
    year: Optional[str] = None

class ChunkDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    document_id: str
    document_title: str
    chunk_index: int
    text: str
    section_ref: Optional[str] = None
    page_number: Optional[int] = 1
    similarity_score: Optional[float] = None
