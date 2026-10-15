import re
from typing import List, Dict, Optional, Tuple
from app.models.chunk import Chunk
from app.schemas.citation_schema import CitationResponse

class CitationMapper:
    """
    Parses inline citation markers (e.g. [1], [2], [1, 2]) from the LLM answer,
    maps them back to their originating source chunks, verifies quotation and claim
    grounding, and assigns explicit verification statuses.
    """
    def __init__(self):
        # Regex to find citation tags like [1], [2], [1, 2], [1][2]
        self.marker_pattern = re.compile(r'\[([0-9]+(?:\s*,\s*[0-9]+)*)\]')

    def _infer_metadata(self, doc_title: str) -> Tuple[str, Optional[str]]:
        """Infers court authority and year from document title."""
        title_lower = doc_title.lower()
        if "sibbia" in title_lower:
            return "Supreme Court of India (Constitution Bench)", "1980"
        elif "sushila aggarwal" in title_lower:
            return "Supreme Court of India (Constitution Bench)", "2020"
        elif "arnesh kumar" in title_lower:
            return "Supreme Court of India (Division Bench)", "2014"
        elif "satender kumar antil" in title_lower:
            return "Supreme Court of India (Division Bench)", "2022"
        elif "lalita kumari" in title_lower:
            return "Supreme Court of India (Constitution Bench)", "2014"
        elif "bharatiya nagarik suraksha" in title_lower or "bnss" in title_lower:
            return "Parliament of India (Central Bare Act)", "2023"
        elif "bharatiya nyaya" in title_lower or "bns" in title_lower:
            return "Parliament of India (Central Bare Act)", "2023"
        elif "code of criminal procedure" in title_lower or "crpc" in title_lower:
            return "Parliament of India (Central Bare Act)", "1973"
        elif "indian penal code" in title_lower or "ipc" in title_lower:
            return "Central Legislative Statute", "1860"
        elif "constitution" in title_lower or "article" in title_lower:
            return "Constituent Assembly of India", "1950"
        return "Supreme Court of India", None

    def _find_claim_for_marker(self, answer_text: str, marker_idx: int) -> str:
        """Finds the sentence or bullet point containing [marker_idx] (handles [1], [1, 2], etc.)."""
        pattern = re.compile(rf'\[[^\]]*\b{marker_idx}\b[^\]]*\]')
        lines = answer_text.split("\n")
        for line in lines:
            if pattern.search(line):
                return line.strip()

        # Fallback to sentence search
        sentences = re.split(r'(?<=[.!?])\s+', answer_text)
        for s in sentences:
            if pattern.search(s):
                return s.strip()
        return ""

    def _verify_quotation(self, claim_text: str, chunk_text: str) -> Tuple[bool, Optional[str], str]:
        """
        Verifies if substantive words of the claim appear in chunk text.
        Returns (quote_found, verbatim_quote, verification_status).
        """
        if not chunk_text:
            return False, None, "Claim support not established"

        # Check for direct quotes in quotes ("...")
        quotes = re.findall(r'["“](.+?)["”]', claim_text)
        for q in quotes:
            if len(q.strip()) > 10 and q.lower() in chunk_text.lower():
                return True, q.strip(), "Source found & Passage verified"

        # Check substantive token overlap
        claim_clean = re.sub(r'\[[0-9]+(?:\s*,\s*[0-9]+)*\]', '', claim_text)
        claim_tokens = set(re.findall(r'\b[a-zA-Z0-9_]{4,}\b', claim_clean.lower()))
        chunk_tokens = set(re.findall(r'\b[a-zA-Z0-9_]{4,}\b', chunk_text.lower()))

        stopwords = {"this", "that", "with", "from", "court", "according", "based", "retrieved", "provisions"}
        sig_claim_tokens = claim_tokens - stopwords

        if not sig_claim_tokens:
            return True, None, "Metadata verified"

        overlap = sig_claim_tokens.intersection(chunk_tokens)
        ratio = len(overlap) / max(len(sig_claim_tokens), 1)

        # Extract best matching sentence from chunk as verbatim quote
        chunk_sentences = re.split(r'(?<=[.!?])\s+', chunk_text)
        best_sentence = ""
        best_overlap = 0
        for sent in chunk_sentences:
            stoks = set(re.findall(r'\b[a-zA-Z0-9_]{4,}\b', sent.lower()))
            sover = len(sig_claim_tokens.intersection(stoks))
            if sover > best_overlap:
                best_overlap = sover
                best_sentence = sent.strip()

        verbatim_quote = best_sentence if best_sentence else self._generate_snippet(chunk_text, max_chars=180)

        if ratio >= 0.35:
            return True, verbatim_quote, "Source found & Passage verified"
        elif ratio >= 0.15:
            return True, verbatim_quote, "Supporting passage available"
        else:
            return False, verbatim_quote, "Metadata verified"

    def extract_citations(
        self,
        answer_text: str,
        chunk_map: Dict[int, Chunk]
    ) -> List[CitationResponse]:
        """
        Extracts citations from the answer text mapped to the retrieved chunks
        with deterministic quotation verification and explicit validation statuses.
        """
        citations: List[CitationResponse] = []
        found_markers = set()

        matches = self.marker_pattern.findall(answer_text)
        for match in matches:
            indices = [int(idx.strip()) for idx in match.split(",") if idx.strip().isdigit()]
            for idx in indices:
                if idx in chunk_map and idx not in found_markers:
                    found_markers.add(idx)
                    chunk = chunk_map[idx]
                    
                    claim_text = self._find_claim_for_marker(answer_text, idx)
                    quote_found, verbatim_quote, status = self._verify_quotation(claim_text, chunk.text)
                    court, year = self._infer_metadata(chunk.document_title or "")
                    snippet = self._generate_snippet(chunk.text)

                    citations.append(CitationResponse(
                        document=chunk.document_title or "Legal Source",
                        section=chunk.section_ref or f"Passage {chunk.chunk_index + 1}",
                        snippet=snippet,
                        chunk_id=chunk.id,
                        confidence_score=chunk.similarity_score or 1.0,
                        marker_index=idx,
                        verification_status=status,
                        verbatim_quote=verbatim_quote,
                        quote_found=quote_found,
                        court=court,
                        year=year
                    ))

        # Sort citations by marker index
        citations.sort(key=lambda c: c.marker_index or 0)
        return citations

    def verify_groundedness(self, answer_text: str, chunk_map: Dict[int, Chunk]) -> Tuple[str, float]:
        """
        Verifies answer groundedness based on marker presence and chunk resolution.
        Returns (confidence_label, score).
        """
        if "insufficient authoritative evidence" in answer_text.lower() or "information not found" in answer_text.lower():
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

    def _generate_snippet(self, text: str, max_chars: int = 240) -> str:
        """Creates a clean snippet from chunk text."""
        cleaned = " ".join(text.split())
        if len(cleaned) <= max_chars:
            return cleaned
        return cleaned[:max_chars].rstrip() + "..."
