from typing import List, Dict, Any
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import QueryLogModel, AnswerModel, CitationModel

router = APIRouter(prefix="/api/logs", tags=["Logs & Evaluation"])

@router.get("")
def get_query_logs(
    limit: int = Query(50, ge=1, le=500),
    db: Session = Depends(get_db)
) -> List[Dict[str, Any]]:
    """
    Export query/answer/citation logs for system evaluation and auditability.
    """
    logs = db.query(QueryLogModel).order_by(QueryLogModel.timestamp.desc()).limit(limit).all()
    results = []
    for log in logs:
        answers = []
        for ans in log.answers:
            citations = [
                {
                    "document": cit.document_title,
                    "section": cit.section_ref,
                    "snippet": cit.snippet,
                    "confidence_score": cit.confidence_score,
                    "chunk_id": cit.chunk_id
                }
                for cit in ans.citations
            ]
            answers.append({
                "id": ans.id,
                "answer_text": ans.answer_text,
                "model_used": ans.model_used,
                "confidence": ans.confidence,
                "citations": citations
            })

        results.append({
            "query_id": log.id,
            "session_id": log.user_session_id,
            "query_text": log.query_text,
            "timestamp": log.timestamp.isoformat() if log.timestamp else None,
            "latency_ms": log.latency_ms,
            "retrieved_count": log.retrieved_count,
            "answers": answers
        })

    return results
