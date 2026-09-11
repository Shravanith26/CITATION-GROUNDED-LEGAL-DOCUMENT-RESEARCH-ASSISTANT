import os
import sys
import argparse

current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(os.path.dirname(current_dir), "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.database.database import init_db, SessionLocal
from app.services.document_service import DocumentService

def ingest_document(file_path: str, title: str = None, doc_type: str = "judgment"):
    init_db()
    db = SessionLocal()
    doc_service = DocumentService()

    print(f"Ingesting document: {file_path}")
    doc = doc_service.ingest_document_file(
        file_path=file_path,
        title=title,
        doc_type=doc_type,
        db=db
    )
    print(f"Ingested successfully: {doc.title} (ID: {doc.id}, Chunks: {doc.total_chunks})")
    db.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest a legal document into the repository.")
    parser.add_argument("file_path", help="Path to document file (TXT or PDF)")
    parser.add_argument("--title", help="Title of the document", default=None)
    parser.add_argument("--type", help="Document type (judgment, statute)", default="judgment")
    args = parser.parse_args()

    ingest_document(args.file_path, args.title, args.type)
