import re
from typing import Dict, List, Optional
from app.utils.logging import ingestion_logger

class LegalNER:
    """
    Extracts structured legal entities such as case names, statutory sections,
    courts, and dates from legal texts using domain rules and regex patterns.
    """
    def __init__(self):
        self.section_pattern = re.compile(
            r'(?:Section|Sec\.|s\.)\s*([0-9]+[A-Za-z]*(?:\([0-9a-zA-Z]+\))*)',
            re.IGNORECASE
        )
        self.article_pattern = re.compile(
            r'(?:Article|Art\.)\s*([0-9]+[A-Za-z]*)',
            re.IGNORECASE
        )
        self.para_pattern = re.compile(
            r'\[(?:Para|Paragraph|Section|Article)\s*([0-9]+[A-Za-z]*(?:\([0-9a-zA-Z]+\))*)\]',
            re.IGNORECASE
        )
        self.citation_pattern = re.compile(
            r'(\([0-9]{4}\)\s*[0-9]+\s*SCC\s*[0-9]+|AIR\s*[0-9]{4}\s*SC\s*[0-9]+|[0-9]{4}\s*SCC\s*OnLine\s*[A-Za-z]+\s*[0-9]+)',
            re.IGNORECASE
        )
        self.court_pattern = re.compile(
            r'(Supreme Court of India|High Court of [A-Za-z ]+|Court of Session|Sessions Court)',
            re.IGNORECASE
        )

    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract legal entities from text."""
        sections = list(set(self.section_pattern.findall(text)))
        articles = list(set(self.article_pattern.findall(text)))
        citations = list(set(self.citation_pattern.findall(text)))
        courts = list(set(self.court_pattern.findall(text)))

        return {
            "sections": [f"Section {s}" for s in sections],
            "articles": [f"Article {a}" for a in articles],
            "citations": citations,
            "courts": courts
        }

    def detect_section_reference(self, chunk_text: str) -> Optional[str]:
        """Identifies the primary section or paragraph label for a chunk."""
        # Check for explicit [Para ...] or [Section ...] headers
        para_match = self.para_pattern.search(chunk_text)
        if para_match:
            return f"Para {para_match.group(1)}"

        # Check for Section references
        sec_match = self.section_pattern.search(chunk_text)
        if sec_match:
            return f"Section {sec_match.group(1)}"

        art_match = self.article_pattern.search(chunk_text)
        if art_match:
            return f"Article {art_match.group(1)}"

        return None
