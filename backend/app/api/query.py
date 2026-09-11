from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.query_schema import QueryRequest
from app.schemas.answer_schema import AnswerResponse
from app.services.rag_service import RAGService

router = APIRouter(prefix="/api/query", tags=["Query"])
rag_service = RAGService()

@router.post("", response_model=AnswerResponse)
def submit_legal_query(
    request: QueryRequest,
    db: Session = Depends(get_db)
):
    """
    Submit a natural-language legal question.
    Returns an answer strictly grounded in retrieved legal documents,
    along with inline citation references mapped to source chunks.
    """
    response = rag_service.process_query(
        query_text=request.query,
        session_id=request.session_id or "default-session",
        top_k=request.top_k or 5,
        db=db
    )
    return response
