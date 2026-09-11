import os
import tempfile
import pytest
from app.services.extraction_service import ExtractionService
from app.services.preprocessing_service import PreprocessingService

def test_extract_plain_text():
    extractor = ExtractionService()
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        f.write("Line 1 of judgment.\nLine 2 of judgment.")
        f_path = f.name

    try:
        pages = extractor.extract_from_file(f_path)
        assert len(pages) == 1
        assert "Line 1" in pages[0]["text"]
        assert pages[0]["page_number"] == 1
    finally:
        os.remove(f_path)

def test_preprocess_metadata_header():
    preprocessor = PreprocessingService()
    sample_raw = (
        "DOCUMENT TITLE: State v. Kumar\n"
        "COURT: Supreme Court of India\n"
        "CITATION: (2020) 1 SCC 100\n"
        "DOCUMENT TYPE: judgment\n\n"
        "Substantive judgment paragraph text goes here."
    )
    meta, content = preprocessor.parse_metadata_headers(sample_raw)
    assert meta["title"] == "State v. Kumar"
    assert meta["court_authority"] == "Supreme Court of India"
    assert meta["citation_ref"] == "(2020) 1 SCC 100"
    assert meta["doc_type"] == "judgment"
    assert "Substantive judgment paragraph text goes here." in content
