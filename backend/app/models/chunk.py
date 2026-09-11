from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Chunk:
    id: str
    document_id: str
    chunk_index: int
    text: str
    section_ref: Optional[str] = None
    page_number: Optional[int] = 1
    embedding_id: Optional[str] = None
    similarity_score: Optional[float] = None
    document_title: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
