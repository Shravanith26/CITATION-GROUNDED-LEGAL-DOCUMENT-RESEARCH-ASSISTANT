from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class DocumentBase(BaseModel):
    title: str
    doc_type: str = Field(default="judgment", description="judgment, statute, regulation")
    court_authority: Optional[str] = None
    citation_ref: Optional[str] = None
    date: Optional[str] = None

class DocumentCreate(DocumentBase):
    content: Optional[str] = None

class DocumentResponse(DocumentBase):
    id: str
    source_path: str
    ingestion_status: str
    total_chunks: int
    created_at: datetime

    class Config:
        from_attributes = True

class DocumentDetailResponse(DocumentResponse):
    full_text: Optional[str] = None
