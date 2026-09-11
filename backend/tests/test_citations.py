import pytest
from app.models.chunk import Chunk
from app.rag.citation_mapper import CitationMapper

def test_citation_mapping_and_snippet_generation():
    mapper = CitationMapper()
    chunk = Chunk(
        id="chunk-abc",
        document_id="doc-xyz",
        chunk_index=0,
        text="A blanket order of anticipatory bail cannot and ought not to be granted as it serves as a charter of lawlessness.",
        section_ref="Para 19",
        document_title="Gurbaksh Singh Sibbia"
    )
    chunk_map = {1: chunk}

    answer_text = "Courts must not issue blanket orders of anticipatory bail [1]."
    citations = mapper.extract_citations(answer_text, chunk_map)

    assert len(citations) == 1
    assert citations[0].document == "Gurbaksh Singh Sibbia"
    assert citations[0].section == "Para 19"
    assert citations[0].chunk_id == "chunk-abc"
    assert "blanket order" in citations[0].snippet.lower()
