import os
from pathlib import Path
from typing import Optional

try:
    from pydantic_settings import BaseSettings
    from pydantic import Field
    _HAS_PYDANTIC_SETTINGS = True
except ImportError:
    _HAS_PYDANTIC_SETTINGS = False

# Resolve project base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Settings:
    """Application configuration settings."""
    def __init__(self):
        # App Info
        self.APP_NAME: str = os.getenv("APP_NAME", "Citation-Grounded Legal Document Research Assistant")
        self.APP_ENV: str = os.getenv("APP_ENV", "development")
        self.DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")
        self.API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
        self.API_PORT: int = int(os.getenv("API_PORT", "8000"))

        # Base Paths
        self.PROJECT_ROOT: Path = BASE_DIR
        self.DATABASE_URL: str = os.getenv(
            "DATABASE_URL", f"sqlite:///{BASE_DIR}/data/metadata/documents.db"
        )
        self.VECTOR_DB_DIR: str = os.getenv(
            "VECTOR_DB_DIR", str(BASE_DIR / "data" / "vector_db" / "chroma")
        )
        self.RAW_DOCUMENTS_DIR: str = os.getenv(
            "RAW_DOCUMENTS_DIR", str(BASE_DIR / "data" / "documents" / "raw")
        )
        self.PROCESSED_DOCUMENTS_DIR: str = os.getenv(
            "PROCESSED_DOCUMENTS_DIR", str(BASE_DIR / "data" / "documents" / "processed")
        )
        self.LOGS_DIR: str = os.getenv("LOGS_DIR", str(BASE_DIR / "logs"))

        # AI / ML Models
        self.EMBEDDING_MODEL_NAME: str = os.getenv(
            "EMBEDDING_MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2"
        )
        self.SPACY_MODEL: str = os.getenv("SPACY_MODEL", "en_core_web_sm")

        # LLM Settings (Ollama)
        self.OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "phi4-mini")
        self.OLLAMA_FALLBACK_MODEL: str = os.getenv("OLLAMA_FALLBACK_MODEL", "llama3.2:3b")
        self.LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", "0.1"))
        self.LLM_TIMEOUT_SECONDS: int = int(os.getenv("LLM_TIMEOUT_SECONDS", "30"))

        # RAG Pipeline Settings
        self.CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "600"))
        self.CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", "100"))
        self.TOP_K_RETRIEVAL: int = int(os.getenv("TOP_K_RETRIEVAL", "5"))
        self.SIMILARITY_THRESHOLD: float = float(os.getenv("SIMILARITY_THRESHOLD", "0.20"))
        self.ENABLE_RERANKING: bool = os.getenv("ENABLE_RERANKING", "True").lower() in ("true", "1", "yes")

        # Ensure required directories exist
        os.makedirs(Path(self.DATABASE_URL.replace("sqlite:///", "")).parent, exist_ok=True)
        os.makedirs(self.VECTOR_DB_DIR, exist_ok=True)
        os.makedirs(self.RAW_DOCUMENTS_DIR, exist_ok=True)
        os.makedirs(self.PROCESSED_DOCUMENTS_DIR, exist_ok=True)
        os.makedirs(self.LOGS_DIR, exist_ok=True)

settings = Settings()
