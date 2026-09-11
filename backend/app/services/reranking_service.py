import re
from typing import List
from app.models.chunk import Chunk
from app.utils.logging import query_logger

class RerankingService:
    """
    Reranks retrieved candidate chunks by combining semantic vector similarity
    with exact legal keyword match boosts (e.g. section numbers, case names).
    """

    def rerank(self, query: str, chunks: List[Chunk]) -> List[Chunk]:
        """Reranks candidate chunks based on composite score."""
        if not chunks or len(chunks) <= 1:
            return chunks

        query_tokens = set(re.findall(r'\b[a-zA-Z0-9_]+\b', query.lower()))
        legal_keywords = {"bail", "anticipatory", "arrest", "custody", "liberty", "section", "article", "condition", "ground"}

        reranked = []
        for chunk in chunks:
            text_tokens = set(re.findall(r'\b[a-zA-Z0-9_]+\b', chunk.text.lower()))
            overlap = query_tokens.intersection(text_tokens)

            # Jaccard overlap ratio
            keyword_score = len(overlap) / max(len(query_tokens), 1)

            # Legal term match bonus
            legal_match = len(overlap.intersection(legal_keywords)) * 0.05

            base_sim = chunk.similarity_score or 0.5
            composite_score = (base_sim * 0.7) + (keyword_score * 0.25) + legal_match

            # Update chunk similarity score with composite score
            chunk.similarity_score = round(min(1.0, composite_score), 4)
            reranked.append(chunk)

        reranked.sort(key=lambda c: c.similarity_score or 0, reverse=True)
        query_logger.info("Reranked retrieved chunks successfully.")
        return reranked
