import re
from typing import Dict, Any, Tuple
from app.utils.logging import ingestion_logger

class PreprocessingService:
    """
    Cleans raw extracted text, extracts embedded metadata headers,
    and removes non-substantive artifacts.
    """

    def clean_text(self, text: str) -> str:
        """Normalizes whitespace, removes redundant formatting artifacts."""
        if not text:
            return ""

        # Normalize unicode quotes and dashes
        text = text.replace('“', '"').replace('”', '"').replace('’', "'").replace('‘', "'")
        text = text.replace('—', '-').replace('–', '-')

        # Replace excessive whitespace while keeping paragraph breaks
        lines = [re.sub(r'[ \t]+', ' ', line).strip() for line in text.splitlines()]
        cleaned = "\n".join(lines)
        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

        return cleaned.strip()

    def parse_metadata_headers(self, text: str) -> Tuple[Dict[str, Any], str]:
        """
        Parses structured metadata headers at the top of documents if present:
        DOCUMENT TITLE: ...
        COURT: ...
        CITATION: ...
        DATE: ...
        DOCUMENT TYPE: ...
        Returns (metadata_dict, remaining_content).
        """
        metadata: Dict[str, Any] = {}
        lines = text.splitlines()
        content_lines = []
        parsing_header = True

        for line in lines:
            if parsing_header:
                match = re.match(r'^(DOCUMENT TITLE|TITLE|COURT|CITATION|BENCH|DATE OF JUDGMENT|DATE|DOCUMENT TYPE|DOC_TYPE):\s*(.+)$', line, re.IGNORECASE)
                if match:
                    key = match.group(1).upper()
                    val = match.group(2).strip()
                    if key in ("DOCUMENT TITLE", "TITLE"):
                        metadata["title"] = val
                    elif key == "COURT":
                        metadata["court_authority"] = val
                    elif key == "CITATION":
                        metadata["citation_ref"] = val
                    elif key in ("DATE OF JUDGMENT", "DATE"):
                        metadata["date"] = val
                    elif key in ("DOCUMENT TYPE", "DOC_TYPE"):
                        metadata["doc_type"] = val.lower()
                    continue
                elif line.strip() == "":
                    continue
                else:
                    parsing_header = False

            content_lines.append(line)

        remaining_text = "\n".join(content_lines).strip()
        return metadata, remaining_text
