import pytest
from app.services.chunking_service import ChunkingService

def test_chunking_preserves_metadata_and_sections():
    service = ChunkingService()
    sample_pages = [
        {
            "page_number": 1,
            "text": (
                "[Para 12]\n"
                "The power under Section 438 is of an extraordinary character and must be exercised with circumspection.\n\n"
                "[Para 15]\n"
                "While considering an application for anticipatory bail, the court must consider the nature and gravity of the accusation."
            )
        }
    ]

    chunks = service.chunk_document(
        document_id="doc-test-123",
        document_title="Sibbia v. State",
        pages=sample_pages
    )

    assert len(chunks) >= 2
    assert chunks[0].document_id == "doc-test-123"
    assert chunks[0].document_title == "Sibbia v. State"
    assert "Para 12" in chunks[0].section_ref
    assert "Section 438" in chunks[0].text
