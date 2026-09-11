import pytest
from app.models.chunk import Chunk
from app.services.retrieval_service import RetrievalService
from app.services.indexing_service import IndexingService
from app.nlp.embeddings import EmbeddingService

def test_semantic_retrieval():
    indexing = IndexingService.get_instance()
    embeddings = EmbeddingService.get_instance()
    retrieval = RetrievalService()

    # Index two sample chunks
    c1 = Chunk(
        id="test-chunk-bail",
        document_id="doc-1",
        chunk_index=0,
        text="The factors to consider for granting anticipatory bail include nature and gravity of accusation.",
        section_ref="Para 15",
        document_title="Sibbia v. State"
    )
    c2 = Chunk(
        id="test-chunk-tax",
        document_id="doc-2",
        chunk_index=0,
        text="Corporate tax filing deadlines are mandated under the income tax assessment act.",
        section_ref="Section 139",
        document_title="Taxation Statute"
    )

    vecs = embeddings.embed_batch([c1.text, c2.text])
    indexing.add_chunks([c1, c2], vecs)

    # Query specifically about anticipatory bail
    results = retrieval.retrieve_top_k("anticipatory bail factors", k=10, threshold=0.0)
    assert len(results) > 0

    # Ensure bail content is ranked prominently
    top_texts = " ".join(r.text.lower() for r in results[:3])
    assert "anticipatory bail" in top_texts

    # Also verify that between c1 and c2, c1 ranks higher
    c1_score = next((r.similarity_score for r in results if r.id == "test-chunk-bail"), 0.0)
    c2_score = next((r.similarity_score for r in results if r.id == "test-chunk-tax"), 0.0)
    assert c1_score >= c2_score
