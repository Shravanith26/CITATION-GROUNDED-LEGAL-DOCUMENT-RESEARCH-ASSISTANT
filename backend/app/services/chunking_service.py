import re
import uuid
from typing import List, Dict, Any
from app.config.config import settings
from app.models.chunk import Chunk
from app.nlp.ner import LegalNER
from app.utils.logging import ingestion_logger

class ChunkingService:
    """
    Segments legal documents into meaningful chunks with metadata preservation:
    parent document ID, paragraph/section reference, page number, and chunk index.
    """

    def __init__(self):
        self.chunk_size = settings.CHUNK_SIZE
        self.chunk_overlap = settings.CHUNK_OVERLAP
        self.ner = LegalNER()

    def chunk_document(
        self,
        document_id: str,
        document_title: str,
        pages: List[Dict[str, Any]]
    ) -> List[Chunk]:
        """
        Chunks a list of extracted pages into structured Chunk objects.
        """
        chunks: List[Chunk] = []
        chunk_idx = 0

        for page in pages:
            page_num = page.get("page_number", 1)
            page_text = page.get("text", "")

            # Split primarily on paragraphs or legal sections
            raw_paragraphs = re.split(r'\n{2,}', page_text)
            current_section_ref = None

            for para in raw_paragraphs:
                para = para.strip()
                if not para:
                    continue

                # Check if paragraph establishes a new section reference
                detected_ref = self.ner.detect_section_reference(para)
                if detected_ref:
                    current_section_ref = detected_ref

                # If paragraph exceeds chunk size, split with overlap
                if len(para) > self.chunk_size:
                    sub_chunks = self._split_with_overlap(para, self.chunk_size, self.chunk_overlap)
                    for sub in sub_chunks:
                        chunk_id = str(uuid.uuid4())
                        chunks.append(Chunk(
                            id=chunk_id,
                            document_id=document_id,
                            chunk_index=chunk_idx,
                            text=sub,
                            section_ref=current_section_ref or f"Para {chunk_idx + 1}",
                            page_number=page_num,
                            document_title=document_title
                        ))
                        chunk_idx += 1
                else:
                    chunk_id = str(uuid.uuid4())
                    chunks.append(Chunk(
                        id=chunk_id,
                        document_id=document_id,
                        chunk_index=chunk_idx,
                        text=para,
                        section_ref=current_section_ref or f"Para {chunk_idx + 1}",
                        page_number=page_num,
                        document_title=document_title
                    ))
                    chunk_idx += 1

        ingestion_logger.info(f"Chunked document '{document_title}' into {len(chunks)} chunks.")
        return chunks

    def _split_with_overlap(self, text: str, max_size: int, overlap: int) -> List[str]:
        """Splits long text into overlapping sliding windows at sentence/word boundaries."""
        words = text.split()
        chunks = []
        current_words = []
        current_len = 0

        for word in words:
            current_words.append(word)
            current_len += len(word) + 1

            if current_len >= max_size:
                chunks.append(" ".join(current_words))
                # Retain overlap words
                overlap_words = []
                overlap_len = 0
                for w in reversed(current_words):
                    if overlap_len + len(w) + 1 <= overlap:
                        overlap_words.insert(0, w)
                        overlap_len += len(w) + 1
                    else:
                        break
                current_words = overlap_words
                current_len = overlap_len

        if current_words:
            chunks.append(" ".join(current_words))

        return chunks
