import pytest
from app.models.chunk import Chunk
from app.services.retrieval_service import RetrievalService
from app.services.reranking_service import RerankingService
from app.services.indexing_service import IndexingService
from app.nlp.embeddings import EmbeddingService

def test_query_expansion():
    retrieval = RetrievalService()
    expanded = retrieval._expand_query("stolen jewellery ring")
    assert "Section 378" in expanded or "Section 303" in expanded or "theft" in expanded

    expanded_bail = retrieval._expand_query("anticipatory bail conditions")
    assert "Section 438" in expanded_bail or "Section 482" in expanded_bail or "Sibbia" in expanded_bail

def test_lexical_scoring():
    retrieval = RetrievalService()
    query_tokens = {"section", "438", "bail", "anticipatory"}
    text = "Section 438 of the Code of Criminal Procedure provides for anticipatory bail."
    meta = {"document_title": "Code of Criminal Procedure", "section_ref": "Section 438"}

    score = retrieval._compute_lexical_score(query_tokens, text, meta)
    assert score > 0.5

def test_reranker_statutory_and_precedent_boost():
    reranker = RerankingService()
    c1 = Chunk(
        id="c1",
        document_id="d1",
        chunk_index=0,
        text="A general discussion about fundamental liberty and detention.",
        section_ref="Article 21",
        document_title="Constitution of India",
        similarity_score=0.70
    )
    c2 = Chunk(
        id="c2",
        document_id="d2",
        chunk_index=0,
        text="Section 438 of CrPC gives power to High Court and Sessions Court for anticipatory bail.",
        section_ref="Section 438",
        document_title="Gurbaksh Singh Sibbia v. State",
        similarity_score=0.65
    )

    query = "What did Gurbaksh Singh Sibbia hold regarding Section 438 anticipatory bail?"
    reranked = reranker.rerank(query, [c1, c2])

    # c2 should be boosted to top rank due to exact Sibbia + Section 438 match
    assert reranked[0].id == "c2"
    assert reranked[0].similarity_score > reranked[1].similarity_score
