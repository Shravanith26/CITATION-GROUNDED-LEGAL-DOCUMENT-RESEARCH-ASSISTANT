import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_documents_list_endpoint():
    response = client.get("/api/documents")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_query_endpoint():
    payload = {
        "query": "What factors are considered while granting anticipatory bail?",
        "top_k": 3
    }
    response = client.post("/api/query", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "citations" in data
    assert "confidence" in data

def test_logs_endpoint():
    response = client.get("/api/logs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
