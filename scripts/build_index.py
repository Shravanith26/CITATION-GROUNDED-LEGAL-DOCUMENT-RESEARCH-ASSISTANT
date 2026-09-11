import os
import sys
import glob

# Ensure backend directory is in path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(os.path.dirname(current_dir), "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.config.config import settings
from app.database.database import init_db, SessionLocal
from app.services.document_service import DocumentService
from app.utils.logging import indexing_logger

def build_index():
    """Initializes DB and builds vector index for all raw legal documents."""
    print("============================================================")
    print(" Building Knowledge Index for Legal Documents")
    print("============================================================")

    init_db()
    db = SessionLocal()
    doc_service = DocumentService()

    raw_files = sorted(glob.glob(os.path.join(settings.RAW_DOCUMENTS_DIR, "*.*")))
    if not raw_files:
        print(f"[WARN] No raw document files found in {settings.RAW_DOCUMENTS_DIR}")
        return

    print(f"[INFO] Found {len(raw_files)} documents to index.")

    for idx, fpath in enumerate(raw_files, start=1):
        fname = os.path.basename(fpath)
        print(f"[{idx}/{len(raw_files)}] Ingesting & indexing: {fname} ...")
        try:
            doc_record = doc_service.ingest_document_file(file_path=fpath, db=db)
            print(f"       -> Indexed '{doc_record.title}' ({doc_record.total_chunks} chunks)")
        except Exception as e:
            print(f"       [ERROR] Failed to index {fname}: {e}")
            indexing_logger.error(f"Error indexing {fname}: {e}", exc_info=True)

    db.close()
    print("============================================================")
    print(" Indexing Complete! Search index is ready for queries.")
    print("============================================================")

if __name__ == "__main__":
    build_index()
