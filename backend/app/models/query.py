from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Query:
    id: str
    query_text: str
    user_session_id: Optional[str] = "default-session"
    timestamp: datetime = field(default_factory=datetime.utcnow)
    latency_ms: Optional[float] = None
    retrieved_count: int = 0
