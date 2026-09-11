from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.schemas.citation_schema import CitationResponse

class AnswerResponse(BaseModel):
    answer: str
    citations: List[CitationResponse] = []
    confidence: str = "grounded"
    model_used: Optional[str] = "phi4-mini"
    query_id: Optional[str] = None
    latency_ms: Optional[float] = None

    class Config:
        from_attributes = True
