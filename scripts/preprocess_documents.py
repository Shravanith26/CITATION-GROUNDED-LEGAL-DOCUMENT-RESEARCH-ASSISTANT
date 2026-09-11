import os
import sys
import glob

current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(os.path.dirname(current_dir), "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.config.config import settings
from app.services.extraction_service import ExtractionService
from app.services.preprocessing_service import PreprocessingService

def preprocess_all():
    print("Preprocessing raw documents...")
    extractor = ExtractionService()
    preprocessor = PreprocessingService()

    raw_files = glob.glob(os.path.join(settings.RAW_DOCUMENTS_DIR, "*.*"))
    for fpath in raw_files:
        fname = os.path.basename(fpath)
        pages = extractor.extract_from_file(fpath)
        raw_combined = "\n\n".join(p["text"] for p in pages)
        meta, cleaned = preprocessor.parse_metadata_headers(raw_combined)
        cleaned = preprocessor.clean_text(cleaned)

        out_path = os.path.join(settings.PROCESSED_DOCUMENTS_DIR, f"cleaned_{fname}")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

        print(f"Preprocessed: {fname} -> {os.path.basename(out_path)} (Length: {len(cleaned)} chars)")

if __name__ == "__main__":
    preprocess_all()
