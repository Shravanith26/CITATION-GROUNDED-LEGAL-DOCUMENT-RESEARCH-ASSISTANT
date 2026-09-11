import pytest
from app.nlp.embeddings import EmbeddingService

def test_embedding_generation_and_normalization():
    service = EmbeddingService.get_instance()
    text = "Section 438 of CrPC deals with anticipatory bail in non-bailable offences."
    vec = service.embed_text(text)

    assert isinstance(vec, list)
    assert len(vec) > 0
    # Check vector has non-zero elements
    assert any(val != 0 for val in vec)
