from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=2, max_length=2000, description="Natural language legal query")
    session_id: Optional[str] = Field(default="default-session", description="User session identifier")
    top_k: Optional[int] = Field(default=5, ge=1, le=20, description="Number of chunks to retrieve")

class QueryLogResponse(BaseModel):
    id: str
    user_session_id: Optional[str]
    query_text: str
    timestamp: datetime
    latency_ms: Optional[float]
    retrieved_count: int

    class Config:
        from_attributes = True
