import os
import sys
import json
import csv
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(os.path.dirname(current_dir), "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.database.database import init_db, SessionLocal
from app.services.rag_service import RAGService
from app.services.retrieval_service import RetrievalService

def run_evaluation():
    print("============================================================")
    print(" Starting Automated Legal RAG Evaluation Suite")
    print("============================================================")

    questions_file = os.path.join(current_dir, "test_questions", "questions.json")
    labels_file = os.path.join(current_dir, "labeled_chunks", "relevance_labels.json")

    with open(questions_file, "r", encoding="utf-8") as f:
        questions = json.load(f)
    with open(labels_file, "r", encoding="utf-8") as f:
        relevance_labels = json.load(f)

    init_db()
    db = SessionLocal()
    rag_service = RAGService()
    retrieval_service = RetrievalService()

    evaluation_rows = []
    retrieval_scores = []
    citation_accuracies = []
    latencies = []
    correct_rejections = 0
    negative_total = 0

    print(f"Running evaluation on {len(questions)} test questions...\n")

    for q in questions:
        qid = q["id"]
        query_text = q["question"]
        label = relevance_labels.get(qid, {})
        target_kw = label.get("target_doc_keyword")

        start = time.time()
        answer_resp = rag_service.process_query(query_text, session_id="eval-session", top_k=5, db=db)
        latency = (time.time() - start) * 1000
        latencies.append(latency)

        retrieved_chunks = retrieval_service.retrieve_top_k(query_text, k=5)

        # Retrieval evaluation
        if target_kw is None:
            negative_total += 1
            is_rejected = "information not found" in answer_resp.answer.lower() or answer_resp.confidence == "insufficient_evidence"
            if is_rejected:
                correct_rejections += 1
            precision_at_k = 1.0 if is_rejected else 0.0
            recall_at_k = 1.0 if is_rejected else 0.0
        else:
            matches = [c for c in retrieved_chunks if target_kw.lower() in (c.document_title or "").lower()]
            precision_at_k = len(matches) / max(len(retrieved_chunks), 1)
            recall_at_k = 1.0 if matches else 0.0

        retrieval_scores.append({"precision": precision_at_k, "recall": recall_at_k})

        # Citation accuracy evaluation
        valid_citations = 0
        total_citations = len(answer_resp.citations)
        for cit in answer_resp.citations:
            if cit.document and cit.snippet:
                valid_citations += 1
        cit_acc = (valid_citations / total_citations) if total_citations > 0 else (1.0 if target_kw is None else 0.0)
        citation_accuracies.append(cit_acc)

        print(f"[{qid}] Query: '{query_text[:50]}...'")
        print(f"      Latency: {latency:.1f}ms | Chunks: {len(retrieved_chunks)} | Citations: {total_citations} | Status: {answer_resp.confidence}")

        evaluation_rows.append({
            "Question ID": qid,
            "Category": q.get("category", "general"),
            "Question": query_text,
            "Precision@5": round(precision_at_k, 2),
            "Recall@5": round(recall_at_k, 2),
            "Citations Count": total_citations,
            "Citation Accuracy": round(cit_acc, 2),
            "Confidence": answer_resp.confidence,
            "Latency (ms)": round(latency, 1),
            "Model": answer_resp.model_used
        })

    db.close()

    # Calculate Aggregate Metrics
    avg_precision = sum(s["precision"] for s in retrieval_scores) / len(retrieval_scores)
    avg_recall = sum(s["recall"] for s in retrieval_scores) / len(retrieval_scores)
    avg_cit_acc = sum(citation_accuracies) / len(citation_accuracies)
    avg_latency = sum(latencies) / len(latencies)
    rejection_acc = (correct_rejections / negative_total) if negative_total > 0 else 1.0

    print("\n============================================================")
    print(" EVALUATION SUMMARY RESULTS")
    print("============================================================")
    print(f" Total Evaluated Queries       : {len(questions)}")
    print(f" Mean Precision@5              : {avg_precision*100:.1f}%")
    print(f" Mean Recall@5                 : {avg_recall*100:.1f}%")
    print(f" Citation Grounding Accuracy   : {avg_cit_acc*100:.1f}%")
    print(f" Negative Query Rejection Rate : {rejection_acc*100:.1f}%")
    print(f" Average End-to-End Latency    : {avg_latency:.1f} ms")
    print("============================================================")

    # Save Results
    results_dir = os.path.join(current_dir, "results")
    report_dir = os.path.join(current_dir, "evaluation_report")
    os.makedirs(results_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)

    with open(os.path.join(results_dir, "retrieval_results.json"), "w") as f:
        json.dump({"mean_precision_at_5": avg_precision, "mean_recall_at_5": avg_recall}, f, indent=2)

    with open(os.path.join(results_dir, "citation_results.json"), "w") as f:
        json.dump({"mean_citation_accuracy": avg_cit_acc}, f, indent=2)

    with open(os.path.join(results_dir, "answer_results.json"), "w") as f:
        json.dump({"negative_rejection_accuracy": rejection_acc, "avg_latency_ms": avg_latency}, f, indent=2)

    csv_path = os.path.join(report_dir, "evaluation_results.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=evaluation_rows[0].keys())
        writer.writeheader()
        writer.writerows(evaluation_rows)

    print(f"Evaluation report saved to: {csv_path}")

if __name__ == "__main__":
    run_evaluation()
