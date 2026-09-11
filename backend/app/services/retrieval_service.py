import numpy as np
from typing import List, Optional
from app.config.config import settings
from app.models.chunk import Chunk
from app.nlp.embeddings import EmbeddingService
from app.services.indexing_service import IndexingService
from app.utils.logging import query_logger

class RetrievalService:
    """
    Performs semantic vector retrieval against indexed legal chunks.
    """
    def __init__(self):
        self.embedding_service = EmbeddingService.get_instance()
        self.indexing_service = IndexingService.get_instance()
        self.similarity_threshold = settings.SIMILARITY_THRESHOLD

    def retrieve_top_k(
        self,
        query_text: str,
        k: Optional[int] = None,
        threshold: Optional[float] = None
    ) -> List[Chunk]:
        """
        Retrieves top-k most semantically relevant chunks for the query text.
        """
        if k is None:
            k = settings.TOP_K_RETRIEVAL
        if threshold is None:
            threshold = self.similarity_threshold

        query_logger.info(f"Retrieving top-{k} chunks for query: '{query_text}'")
        query_vector = self.embedding_service.embed_text(query_text)

        chunks: List[Chunk] = []

        if not self.indexing_service.use_fallback and self.indexing_service.collection is not None:
            results = self.indexing_service.collection.query(
                query_embeddings=[query_vector],
                n_results=k,
                include=["documents", "metadatas", "distances"]
            )
            
            ids = results["ids"][0] if results.get("ids") else []
            docs = results["documents"][0] if results.get("documents") else []
            metadatas = results["metadatas"][0] if results.get("metadatas") else []
            distances = results["distances"][0] if results.get("distances") else []

            for i in range(len(ids)):
                # Chroma cosine distance = 1 - cosine_similarity
                distance = distances[i] if i < len(distances) else 1.0
                similarity = max(0.0, 1.0 - distance)
                
                if similarity < threshold:
                    continue

                meta = metadatas[i] if i < len(metadatas) else {}
                chunks.append(Chunk(
                    id=ids[i],
                    document_id=meta.get("document_id", ""),
                    chunk_index=meta.get("chunk_index", 0),
                    text=docs[i] if i < len(docs) else "",
                    section_ref=meta.get("section_ref", ""),
                    page_number=meta.get("page_number", 1),
                    document_title=meta.get("document_title", ""),
                    similarity_score=round(float(similarity), 4)
                ))
        else:
            # Fallback retrieval using cosine similarity over local store
            store = self.indexing_service._load_fallback_store()
            if not store:
                query_logger.warning("Local fallback vector store is empty.")
                return []

            q_vec = np.array(query_vector, dtype=np.float32)
            q_norm = np.linalg.norm(q_vec)
            if q_norm > 0:
                q_vec = q_vec / q_norm

            scored = []
            for chunk_id, data in store.items():
                c_vec = np.array(data["embedding"], dtype=np.float32)
                c_norm = np.linalg.norm(c_vec)
                if c_norm > 0:
                    c_vec = c_vec / c_norm
                
                sim = float(np.dot(q_vec, c_vec))
                if sim >= threshold:
                    scored.append((sim, chunk_id, data))

            scored.sort(key=lambda x: x[0], reverse=True)
            for sim, chunk_id, data in scored[:k]:
                meta = data.get("metadata", {})
                chunks.append(Chunk(
                    id=chunk_id,
                    document_id=meta.get("document_id", ""),
                    chunk_index=meta.get("chunk_index", 0),
                    text=data.get("document", ""),
                    section_ref=meta.get("section_ref", ""),
                    page_number=meta.get("page_number", 1),
                    document_title=meta.get("document_title", ""),
                    similarity_score=round(float(sim), 4)
                ))

        query_logger.info(f"Retrieved {len(chunks)} relevant chunks above threshold {threshold}.")
        return chunks
