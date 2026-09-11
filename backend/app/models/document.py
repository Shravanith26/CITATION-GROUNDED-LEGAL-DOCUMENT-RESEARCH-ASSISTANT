from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class Document:
    id: str
    title: str
    doc_type: str  # judgment, statute, regulation
    court_authority: Optional[str] = None
    citation_ref: Optional[str] = None
    date: Optional[str] = None
    source_path: str = ""
    ingestion_status: str = "indexed"
    total_chunks: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)
