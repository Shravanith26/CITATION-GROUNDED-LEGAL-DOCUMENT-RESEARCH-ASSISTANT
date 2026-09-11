from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class Answer:
    id: str
    query_id: str
    answer_text: str
    model_used: str = "phi4-mini"
    confidence: str = "grounded"
    generated_at: datetime = field(default_factory=datetime.utcnow)
