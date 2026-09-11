import re
from typing import List, Dict, Optional, Tuple
from app.models.chunk import Chunk
from app.schemas.citation_schema import CitationResponse

class CitationMapper:
    """
    Parses inline citation markers (e.g. [1], [2], [1, 2]) from the LLM answer,
    maps them back to their originating source chunks, and verifies faithfulness.
    """
    def __init__(self):
        # Regex to find citation tags like [1], [2], [1, 2], [1][2]
        self.marker_pattern = re.compile(r'\[([0-9]+(?:\s*,\s*[0-9]+)*)\]')

    def extract_citations(
        self,
        answer_text: str,
        chunk_map: Dict[int, Chunk]
    ) -> List[CitationResponse]:
        """
        Extracts citations from the answer text mapped to the retrieved chunks.
        """
        citations: List[CitationResponse] = []
        found_markers = set()

        matches = self.marker_pattern.findall(answer_text)
        for match in matches:
            # Handle comma-separated indices like [1, 2]
            indices = [int(idx.strip()) for idx in match.split(",") if idx.strip().isdigit()]
            for idx in indices:
                if idx in chunk_map and idx not in found_markers:
                    found_markers.add(idx)
                    chunk = chunk_map[idx]
                    
                    # Generate concise snippet (up to 200 chars)
                    snippet = self._generate_snippet(chunk.text)
                    
                    citations.append(CitationResponse(
                        document=chunk.document_title or "Legal Source",
                        section=chunk.section_ref or f"Passage {chunk.chunk_index + 1}",
                        snippet=snippet,
                        chunk_id=chunk.id,
                        confidence_score=chunk.similarity_score or 1.0,
                        marker_index=idx
                    ))

        # Sort citations by marker index
        citations.sort(key=lambda c: c.marker_index or 0)
        return citations

    def verify_groundedness(self, answer_text: str, chunk_map: Dict[int, Chunk]) -> Tuple[str, float]:
        """
        Verifies answer groundedness.
        Returns (confidence_label, score).
        """
        if "information not found" in answer_text.lower():
            return "insufficient_evidence", 0.0

        matches = self.marker_pattern.findall(answer_text)
        if not matches and chunk_map:
            return "unsupported_claims", 0.3

        valid_markers = 0
        total_markers = 0
        for match in matches:
            indices = [int(idx.strip()) for idx in match.split(",") if idx.strip().isdigit()]
            for idx in indices:
                total_markers += 1
                if idx in chunk_map:
                    valid_markers += 1

        if total_markers == 0:
            return "unsupported_claims", 0.2

        score = valid_markers / total_markers
        if score >= 0.8:
            return "grounded", score
        else:
            return "partially_grounded", score

    def _generate_snippet(self, text: str, max_chars: int = 220) -> str:
        """Creates a clean snippet from chunk text."""
        cleaned = " ".join(text.split())
        if len(cleaned) <= max_chars:
            return cleaned
        return cleaned[:max_chars].rstrip() + "..."
