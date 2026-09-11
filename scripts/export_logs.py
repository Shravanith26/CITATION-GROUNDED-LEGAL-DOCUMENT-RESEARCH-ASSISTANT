import os
import sys
import csv

current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(os.path.dirname(current_dir), "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.database.database import SessionLocal
from app.database.models import QueryLogModel, AnswerModel, CitationModel

def export_logs_to_csv():
    db = SessionLocal()
    out_file = os.path.join(os.path.dirname(current_dir), "evaluation", "evaluation_report", "query_logs_export.csv")
    os.makedirs(os.path.dirname(out_file), exist_ok=True)

    queries = db.query(QueryLogModel).all()
    print(f"Exporting {len(queries)} query logs to {out_file}...")

    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Query ID", "Timestamp", "User Query", "Latency (ms)", 
            "Retrieved Chunks", "Confidence", "Answer Text", "Citations Count"
        ])

        for q in queries:
            for ans in q.answers:
                writer.writerow([
                    q.id,
                    q.timestamp.isoformat() if q.timestamp else "",
                    q.query_text,
                    q.latency_ms,
                    q.retrieved_count,
                    ans.confidence,
                    ans.answer_text.replace("\n", " "),
                    len(ans.citations)
                ])

    db.close()
    print("Export complete!")

if __name__ == "__main__":
    export_logs_to_csv()
