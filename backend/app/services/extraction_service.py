import os
from typing import List, Dict, Any
from app.utils.logging import ingestion_logger

class ExtractionService:
    """
    Extracts text content from various file formats (TXT, PDF, MD)
    with page number and layout tracking.
    """

    def extract_from_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Extracts pages from the given file path.
        Returns a list of dicts: [{'page_number': 1, 'text': '...'}]
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        ext = os.path.splitext(file_path)[1].lower()

        if ext in (".txt", ".md"):
            return self._extract_text_file(file_path)
        elif ext == ".pdf":
            return self._extract_pdf_file(file_path)
        else:
            # Attempt plain text read as fallback
            return self._extract_text_file(file_path)

    def _extract_text_file(self, file_path: str) -> List[Dict[str, Any]]:
        ingestion_logger.info(f"Extracting plain text file: {file_path}")
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Handle explicit [Page X] markers if present, or treat as page 1
        pages = []
        if "[Page " in content:
            parts = content.split("[Page ")
            for i, part in enumerate(parts):
                if not part.strip():
                    continue
                pages.append({"page_number": i, "text": part})
        else:
            pages.append({"page_number": 1, "text": content})

        return pages

    def _extract_pdf_file(self, file_path: str) -> List[Dict[str, Any]]:
        ingestion_logger.info(f"Extracting PDF file: {file_path}")
        pages = []

        # Try pypdf first
        try:
            from pypdf import PdfReader
            reader = PdfReader(file_path)
            for idx, page in enumerate(reader.pages, start=1):
                page_text = page.extract_text() or ""
                pages.append({"page_number": idx, "text": page_text})
            if pages:
                return pages
        except Exception as e:
            ingestion_logger.warning(f"pypdf extraction failed ({e}), trying PyMuPDF...")

        # Try PyMuPDF (fitz)
        try:
            import fitz
            doc = fitz.open(file_path)
            for idx in range(len(doc)):
                page = doc[idx]
                page_text = page.get_text() or ""
                pages.append({"page_number": idx + 1, "text": page_text})
            doc.close()
            if pages:
                return pages
        except Exception as e:
            ingestion_logger.warning(f"PyMuPDF extraction failed ({e})")

        # Fallback if libraries not yet installed
        with open(file_path, "rb") as f:
            raw_bytes = f.read()
            # Basic textual string extraction
            extracted = "".join(chr(b) if 32 <= b <= 126 or b in (10, 13) else " " for b in raw_bytes[:100000])
            pages.append({"page_number": 1, "text": extracted})

        return pages
