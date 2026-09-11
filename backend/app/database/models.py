import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Integer, Float, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.database.database import Base

def generate_uuid() -> str:
    return str(uuid.uuid4())

class DocumentModel(Base):
    __tablename__ = "documents"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    title = Column(String(512), nullable=False, index=True)
    doc_type = Column(String(64), nullable=False, default="judgment", index=True)  # judgment, statute, regulation
    court_authority = Column(String(256), nullable=True, index=True)
    citation_ref = Column(String(256), nullable=True)
    date = Column(String(64), nullable=True, index=True)
    source_path = Column(String(1024), nullable=False)
    ingestion_status = Column(String(64), default="indexed")  # pending, indexed, failed
    total_chunks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    chunks = relationship("ChunkModel", back_populates="document", cascade="all, delete-orphan")


class ChunkModel(Base):
    __tablename__ = "chunks"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    document_id = Column(String(36), ForeignKey("documents.id", ondelete="CASCADE"), nullable=False, index=True)
    chunk_index = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    section_ref = Column(String(256), nullable=True)  # e.g., "Para 15", "Section 438(1)"
    page_number = Column(Integer, nullable=True, default=1)
    embedding_id = Column(String(128), nullable=True)  # Key in vector database
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    document = relationship("DocumentModel", back_populates="chunks")
    citations = relationship("CitationModel", back_populates="chunk")


class QueryLogModel(Base):
    __tablename__ = "query_logs"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_session_id = Column(String(128), nullable=True, default="default-session")
    query_text = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    latency_ms = Column(Float, nullable=True)
    retrieved_count = Column(Integer, default=0)

    # Relationships
    answers = relationship("AnswerModel", back_populates="query", cascade="all, delete-orphan")


class AnswerModel(Base):
    __tablename__ = "answers"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    query_id = Column(String(36), ForeignKey("query_logs.id", ondelete="CASCADE"), nullable=False, index=True)
    answer_text = Column(Text, nullable=False)
    model_used = Column(String(128), nullable=False, default="phi4-mini")
    confidence = Column(String(64), default="grounded")  # grounded, insufficient_evidence, fallback
    generated_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    query = relationship("QueryLogModel", back_populates="answers")
    citations = relationship("CitationModel", back_populates="answer", cascade="all, delete-orphan")


class CitationModel(Base):
    __tablename__ = "citations"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    answer_id = Column(String(36), ForeignKey("answers.id", ondelete="CASCADE"), nullable=False, index=True)
    chunk_id = Column(String(36), ForeignKey("chunks.id", ondelete="SET NULL"), nullable=True, index=True)
    document_title = Column(String(512), nullable=True)
    section_ref = Column(String(256), nullable=True)
    snippet = Column(Text, nullable=True)
    confidence_score = Column(Float, default=1.0)
    marker_index = Column(Integer, default=1)  # e.g., 1 for [1], 2 for [2]
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    answer = relationship("AnswerModel", back_populates="citations")
    chunk = relationship("ChunkModel", back_populates="citations")
