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
    assert citations[0].quote_found is True
    assert "Passage verified" in citations[0].verification_status

def test_compound_citation_markers_and_quote_verification():
    mapper = CitationMapper()
    c1 = Chunk(
        id="c1",
        document_id="d1",
        chunk_index=0,
        text="A blanket order of anticipatory bail cannot be granted under Section 438.",
        section_ref="Para 19",
        document_title="Sibbia v. State"
    )
    c2 = Chunk(
        id="c2",
        document_id="d2",
        chunk_index=0,
        text="Anticipatory bail should not ordinarily be limited to a fixed duration.",
        section_ref="Para 63",
        document_title="Sushila Aggarwal v. State"
    )
    chunk_map = {1: c1, 2: c2}

    # Test compound marker [1, 2]
    answer_text = "The Supreme Court ruled that blanket orders cannot be granted and bail duration should not be limited [1, 2]."
    citations = mapper.extract_citations(answer_text, chunk_map)

    assert len(citations) == 2
    assert citations[0].marker_index == 1
    assert citations[0].quote_found is True
    assert citations[1].marker_index == 2
    assert citations[1].quote_found is True
    assert "Passage verified" in citations[0].verification_status
    assert "Passage verified" in citations[1].verification_status

