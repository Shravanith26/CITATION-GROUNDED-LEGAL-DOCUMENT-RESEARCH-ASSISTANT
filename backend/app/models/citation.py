from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Citation:
    id: str
    answer_id: str
    chunk_id: Optional[str] = None
    document_title: Optional[str] = None
    section_ref: Optional[str] = None
    snippet: Optional[str] = None
    confidence_score: float = 1.0
    marker_index: int = 1
    created_at: datetime = field(default_factory=datetime.utcnow)
