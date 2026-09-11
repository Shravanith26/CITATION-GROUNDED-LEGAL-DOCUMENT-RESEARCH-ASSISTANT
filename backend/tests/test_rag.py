import pytest
from app.models.chunk import Chunk
from app.rag.context_builder import ContextBuilder
from app.services.rag_service import RAGService

def test_context_builder_blocks():
    chunks = [
        Chunk(
            id="c1",
            document_id="d1",
            chunk_index=0,
            text="Anticipatory bail protects personal liberty under Article 21.",
            section_ref="Para 7",
            document_title="Sibbia Precedent"
        )
    ]
    context_str, chunk_map = ContextBuilder.build_context(chunks)
    assert "[1] Source Document: Sibbia Precedent" in context_str
    assert "Section/Paragraph: Para 7" in context_str
    assert 1 in chunk_map

def test_negative_query_rejection():
    rag = RAGService()
    # Test completely ungrounded out-of-scope question
    resp = rag.process_query("How to bake a chocolate cake recipe?")
    assert "Information not found" in resp.answer
    assert resp.confidence in ("insufficient_evidence", "grounded")
