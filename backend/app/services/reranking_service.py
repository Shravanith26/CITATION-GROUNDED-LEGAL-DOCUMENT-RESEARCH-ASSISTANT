import re
from typing import List
from app.models.chunk import Chunk
from app.utils.logging import query_logger

class RerankingService:
    """
    Reranks retrieved candidate chunks by combining semantic vector similarity
    with exact legal statutory section matches, case name matches, and domain taxonomy.
    """

    def rerank(self, query: str, chunks: List[Chunk]) -> List[Chunk]:
        """Reranks candidate chunks based on composite score."""
        if not chunks or len(chunks) <= 1:
            return chunks

        query_lower = query.lower()
        query_tokens = set(re.findall(r'\b[a-zA-Z0-9_]+\b', query_lower))

        # Important statutory section numbers and Acts
        statutory_patterns = re.findall(r'\b(?:section|s\.|article|art\.)\s*(\d+[a-z]?|\d+)\b', query_lower)
        case_names = ["sibbia", "arnesh", "sushila", "antil", "lalita", "satender"]

        # Legal domain keywords
        legal_keywords = {
            "bail", "anticipatory", "arrest", "custody", "liberty", "section", "article",
            "condition", "ground", "fir", "cognizable", "theft", "cheating", "quash",
            "magistrate", "investigation", "chargesheet", "remand", "summons", "warrant",
            "bns", "bnss", "crpc", "ipc", "bsa"
        }

        reranked = []
        for chunk in chunks:
            text_lower = chunk.text.lower()
            doc_lower = (chunk.document_title or "").lower()
            sec_lower = (chunk.section_ref or "").lower()
            combined_text = f"{text_lower} {doc_lower} {sec_lower}"

            chunk_tokens = set(re.findall(r'\b[a-zA-Z0-9_]+\b', combined_text))
            overlap = query_tokens.intersection(chunk_tokens)

            # Jaccard overlap ratio
            keyword_score = len(overlap) / max(len(query_tokens), 1)

            # Legal term match bonus
            legal_match = len(overlap.intersection(legal_keywords)) * 0.04

            # Statutory section exact match bonus
            section_bonus = 0.0
            for sec in statutory_patterns:
                if sec in sec_lower or f"section {sec}" in combined_text or f"s. {sec}" in combined_text:
                    section_bonus += 0.15

            # Precedent name exact match bonus
            precedent_bonus = 0.0
            for name in case_names:
                if name in query_lower and name in doc_lower:
                    precedent_bonus += 0.15

            base_sim = chunk.similarity_score or 0.5
            composite_score = (base_sim * 0.6) + (keyword_score * 0.2) + legal_match + section_bonus + precedent_bonus

            # Update chunk similarity score with composite score (capped at 1.0)
            chunk.similarity_score = round(min(1.0, max(0.0, composite_score)), 4)
            reranked.append(chunk)

        reranked.sort(key=lambda c: c.similarity_score or 0, reverse=True)
        query_logger.info(f"Reranked {len(reranked)} retrieved chunks successfully.")
        return reranked
