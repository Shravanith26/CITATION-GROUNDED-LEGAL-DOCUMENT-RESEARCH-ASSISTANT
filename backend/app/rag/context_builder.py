from typing import List, Dict, Any, Tuple
from app.models.chunk import Chunk

class ContextBuilder:
    """
    Assembles retrieved chunks into structured context blocks for the LLM prompt,
    and maintains index mappings between prompt citation numbers and source chunk objects.
    """

    @staticmethod
    def build_context(chunks: List[Chunk]) -> Tuple[str, Dict[int, Chunk]]:
        """
        Builds a numbered context string and returns (context_str, index_to_chunk_map).
        """
        if not chunks:
            return "No relevant legal passages found.", {}

        context_blocks = []
        chunk_map: Dict[int, Chunk] = {}

        for idx, chunk in enumerate(chunks, start=1):
            chunk_map[idx] = chunk
            doc_title = chunk.document_title or "Legal Source"
            sec_ref = chunk.section_ref or f"Passage {chunk.chunk_index + 1}"
            
            block = (
                f"[{idx}] Source Document: {doc_title}\n"
                f"Section/Paragraph: {sec_ref}\n"
                f"Content:\n{chunk.text.strip()}\n"
            )
            context_blocks.append(block)

        context_str = "\n---\n".join(context_blocks)
        return context_str, chunk_map
