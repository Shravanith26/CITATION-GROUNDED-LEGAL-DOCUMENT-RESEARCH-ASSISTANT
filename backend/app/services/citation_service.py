from typing import List, Dict, Tuple
from sqlalchemy.orm import Session
from app.models.chunk import Chunk
from app.rag.citation_mapper import CitationMapper
from app.schemas.citation_schema import CitationResponse
from app.database.models import CitationModel
from app.utils.logging import query_logger

class CitationService:
    """
    Orchestrates citation extraction, validation, and database persistence.
    """
    def __init__(self):
        self.mapper = CitationMapper()

    def process_citations(
        self,
        answer_text: str,
        chunk_map: Dict[int, Chunk],
        answer_id: str = None,
        db: Session = None
    ) -> Tuple[List[CitationResponse], str]:
        """
        Extracts citations from generated answer and optionally saves them to DB.
        Returns (citations_list, confidence_status).
        """
        citations = self.mapper.extract_citations(answer_text, chunk_map)
        confidence, score = self.mapper.verify_groundedness(answer_text, chunk_map)

        query_logger.info(
            f"Extracted {len(citations)} citations. Groundedness confidence: {confidence} (score: {score})"
        )

        if db and answer_id and citations:
            for cit in citations:
                cit_record = CitationModel(
                    answer_id=answer_id,
                    chunk_id=cit.chunk_id,
                    document_title=cit.document,
                    section_ref=cit.section,
                    snippet=cit.snippet,
                    confidence_score=cit.confidence_score or 1.0,
                    marker_index=cit.marker_index or 1
                )
                db.add(cit_record)
            db.commit()

        return citations, confidence
