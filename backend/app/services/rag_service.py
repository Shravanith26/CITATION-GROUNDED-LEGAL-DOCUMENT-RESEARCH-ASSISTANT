import time
import uuid
from typing import Optional
from sqlalchemy.orm import Session
from app.config.config import settings
from app.services.retrieval_service import RetrievalService
from app.services.reranking_service import RerankingService
from app.services.llm_service import LLMService
from app.services.citation_service import CitationService
from app.rag.context_builder import ContextBuilder
from app.rag.prompt_templates import LEGAL_SYSTEM_PROMPT, LEGAL_RAG_USER_PROMPT
from app.schemas.answer_schema import AnswerResponse
from app.database.models import QueryLogModel, AnswerModel
from app.utils.logging import query_logger

class RAGService:
    """
    End-to-end Retrieval-Augmented Generation service orchestrator.
    """
    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.reranking_service = RerankingService()
        self.llm_service = LLMService()
        self.citation_service = CitationService()

    def process_query(
        self,
        query_text: str,
        session_id: str = "default-session",
        top_k: Optional[int] = None,
        db: Optional[Session] = None
    ) -> AnswerResponse:
        """
        Executes the RAG pipeline for a given user query.
        """
        start_time = time.time()
        query_logger.info(f"Processing query: '{query_text}' (session: {session_id})")

        # 1. Semantic vector retrieval
        chunks = self.retrieval_service.retrieve_top_k(query_text, k=top_k)

        # 2. Optional reranking
        if settings.ENABLE_RERANKING and chunks:
            chunks = self.reranking_service.rerank(query_text, chunks)

        # 3. Check for insufficient context
        if not chunks:
            latency_ms = round((time.time() - start_time) * 1000, 2)
            answer_text = "Information not found in the provided legal context."
            
            # Persist query log if db is available
            query_id = None
            if db:
                query_log = QueryLogModel(
                    user_session_id=session_id,
                    query_text=query_text,
                    latency_ms=latency_ms,
                    retrieved_count=0
                )
                db.add(query_log)
                db.commit()
                db.refresh(query_log)
                query_id = query_log.id

                ans_model = AnswerModel(
                    query_id=query_id,
                    answer_text=answer_text,
                    model_used="none",
                    confidence="insufficient_evidence"
                )
                db.add(ans_model)
                db.commit()

            return AnswerResponse(
                answer=answer_text,
                citations=[],
                confidence="insufficient_evidence",
                model_used="none",
                query_id=query_id,
                latency_ms=latency_ms
            )

        # 4. Assemble context & mappings
        context_str, chunk_map = ContextBuilder.build_context(chunks)
        user_prompt = LEGAL_RAG_USER_PROMPT.format(context=context_str, query=query_text)

        # 5. LLM Inference
        raw_answer, model_used = self.llm_service.generate(
            system_prompt=LEGAL_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            chunks=chunks
        )

        latency_ms = round((time.time() - start_time) * 1000, 2)

        # 6. Database Logging
        query_id = None
        answer_id = None
        if db:
            query_log = QueryLogModel(
                user_session_id=session_id,
                query_text=query_text,
                latency_ms=latency_ms,
                retrieved_count=len(chunks)
            )
            db.add(query_log)
            db.commit()
            db.refresh(query_log)
            query_id = query_log.id

            ans_record = AnswerModel(
                query_id=query_id,
                answer_text=raw_answer,
                model_used=model_used,
                confidence="grounded"
            )
            db.add(ans_record)
            db.commit()
            db.refresh(ans_record)
            answer_id = ans_record.id

        # 7. Extract & verify citations
        citations, confidence = self.citation_service.process_citations(
            answer_text=raw_answer,
            chunk_map=chunk_map,
            answer_id=answer_id,
            db=db
        )

        # Update answer confidence if verified
        if db and answer_id:
            ans_record.confidence = confidence
            db.commit()

        return AnswerResponse(
            answer=raw_answer,
            citations=citations,
            confidence=confidence,
            model_used=model_used,
            query_id=query_id,
            latency_ms=latency_ms
        )
