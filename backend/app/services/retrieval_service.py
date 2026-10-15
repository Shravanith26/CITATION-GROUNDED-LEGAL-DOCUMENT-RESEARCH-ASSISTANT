import re
import numpy as np
from typing import List, Optional, Dict, Tuple
from app.config.config import settings
from app.models.chunk import Chunk
from app.nlp.embeddings import EmbeddingService
from app.services.indexing_service import IndexingService
from app.utils.logging import query_logger

class RetrievalService:
    """
    Performs hybrid retrieval (Dense Vector + Lexical Token Scoring + RRF)
    against indexed legal chunks across ChromaDB and local fallback stores.
    """
    def __init__(self):
        self.embedding_service = EmbeddingService.get_instance()
        self.indexing_service = IndexingService.get_instance()
        self.similarity_threshold = settings.SIMILARITY_THRESHOLD

    def _expand_query(self, query_text: str) -> str:
        """Expands user query with Indian legal statutory concordance and synonym terms."""
        expanded = query_text
        lowered = query_text.lower()

        # Theft, snatching & stolen property
        if re.search(r'\b(stollen|stole|stolen|robbed|snatched|thief|theft)\b', lowered):
            expanded += " theft stolen property movable property Section 378 Section 379 IPC Section 303 Section 304 BNS FIR Section 154 CrPC Section 173 BNSS"
        # Valuables & movable objects
        if re.search(r'\b(ring|jewellery|gold|phone|mobile|purse|vehicle|bike|car)\b', lowered):
            expanded += " movable property theft Section 378 IPC Section 303 BNS"
        # Cheating & cyber fraud
        if re.search(r'\b(cheated|scam|fraud|scammed)\b', lowered):
            expanded += " cheating fraud dishonestly inducing delivery of property Section 415 Section 420 IPC Section 318 BNS"
        # FIR & Police reporting
        if re.search(r'\b(fir|police complaint|report to police)\b', lowered):
            expanded += " First Information Report Section 154 CrPC Section 173 BNSS mandatory Lalita Kumari cognizable offence"
        # Anticipatory Bail
        if re.search(r'\b(anticipatory bail|pre-arrest bail|apprehending arrest)\b', lowered):
            expanded += " anticipatory bail Section 438 CrPC Section 482 BNSS Gurbaksh Singh Sibbia Sushila Aggarwal Article 21"
        # Arrest & S. 41A Checklist
        if re.search(r'\b(arrest|notice of appearance|checklist)\b', lowered):
            expanded += " arrest guidelines Section 41 Section 41A CrPC Section 35 BNSS Arnesh Kumar checklist Magistrate"
        # Bail categorisation & guidelines
        if re.search(r'\b(bail guidelines|category a|category b|antil)\b', lowered):
            expanded += " Satender Kumar Antil bail categories undertrial detention"

        return expanded

    def _compute_lexical_score(self, query_tokens: set, text: str, meta: dict) -> float:
        """Computes lexical term match and weighted legal statutory keyword score."""
        if not text:
            return 0.0

        text_lower = text.lower()
        title_lower = (meta.get("document_title") or "").lower()
        sec_lower = (meta.get("section_ref") or "").lower()
        full_text = f"{text_lower} {title_lower} {sec_lower}"

        doc_tokens = set(re.findall(r'\b[a-zA-Z0-9_]+\b', full_text))
        if not doc_tokens:
            return 0.0

        overlap = query_tokens.intersection(doc_tokens)
        base_overlap = len(overlap) / max(len(query_tokens), 1)

        # High-value statutory and legal keywords boost
        statutory_tokens = {"section", "article", "bail", "anticipatory", "arrest", "fir", "theft", "cheating",
                            "438", "482", "378", "379", "303", "304", "41a", "154", "173", "420", "318",
                            "sibbia", "arnesh", "sushila", "antil", "bns", "bnss", "crpc", "ipc"}
        statutory_overlap = len(overlap.intersection(statutory_tokens))
        statutory_bonus = statutory_overlap * 0.12

        return min(1.0, base_overlap + statutory_bonus)

    def retrieve_top_k(
        self,
        query_text: str,
        k: Optional[int] = None,
        threshold: Optional[float] = None
    ) -> List[Chunk]:
        """
        Retrieves top-k chunks using hybrid dense + lexical ranking with Reciprocal Rank Fusion.
        """
        if k is None:
            k = settings.TOP_K_RETRIEVAL
        if threshold is None:
            threshold = self.similarity_threshold

        expanded_query = self._expand_query(query_text)
        query_tokens = set(re.findall(r'\b[a-zA-Z0-9_]+\b', expanded_query.lower()))
        # Filter out common short stopwords
        stopwords = {"what", "which", "when", "where", "how", "does", "can", "the", "and", "for", "with", "from", "are", "is", "a", "an", "in", "to", "of", "or"}
        query_tokens = query_tokens - stopwords

        query_logger.info(f"Retrieving top-{k} chunks for query: '{query_text}'")
        query_vector = self.embedding_service.embed_text(expanded_query)

        candidate_chunks: List[Tuple[Chunk, float, float]] = [] # (Chunk, dense_sim, lexical_score)

        if not self.indexing_service.use_fallback and self.indexing_service.collection is not None:
            # Query Chroma with a wider candidate pool
            fetch_k = max(k * 4, 20)
            results = self.indexing_service.collection.query(
                query_embeddings=[query_vector],
                n_results=fetch_k,
                include=["documents", "metadatas", "distances"]
            )

            ids = results["ids"][0] if results.get("ids") else []
            docs = results["documents"][0] if results.get("documents") else []
            metadatas = results["metadatas"][0] if results.get("metadatas") else []
            distances = results["distances"][0] if results.get("distances") else []

            for i in range(len(ids)):
                distance = distances[i] if i < len(distances) else 1.0
                dense_sim = max(0.0, 1.0 - distance)
                meta = metadatas[i] if i < len(metadatas) else {}
                text = docs[i] if i < len(docs) else ""
                lexical_sim = self._compute_lexical_score(query_tokens, text, meta)

                chunk = Chunk(
                    id=ids[i],
                    document_id=meta.get("document_id", ""),
                    chunk_index=meta.get("chunk_index", 0),
                    text=text,
                    section_ref=meta.get("section_ref", ""),
                    page_number=meta.get("page_number", 1),
                    document_title=meta.get("document_title", ""),
                    similarity_score=round(float(dense_sim), 4)
                )
                candidate_chunks.append((chunk, dense_sim, lexical_sim))
        else:
            # Local in-memory fallback store
            store = self.indexing_service._load_fallback_store()
            if not store:
                query_logger.warning("Local fallback vector store is empty.")
                return []

            q_vec = np.array(query_vector, dtype=np.float32)
            q_norm = np.linalg.norm(q_vec)
            if q_norm > 0:
                q_vec = q_vec / q_norm

            for chunk_id, data in store.items():
                c_vec = np.array(data["embedding"], dtype=np.float32)
                c_norm = np.linalg.norm(c_vec)
                if c_norm > 0:
                    c_vec = c_vec / c_norm

                dense_sim = float(np.dot(q_vec, c_vec))
                meta = data.get("metadata", {})
                text = data.get("document", "")
                lexical_sim = self._compute_lexical_score(query_tokens, text, meta)

                chunk = Chunk(
                    id=chunk_id,
                    document_id=meta.get("document_id", ""),
                    chunk_index=meta.get("chunk_index", 0),
                    text=text,
                    section_ref=meta.get("section_ref", ""),
                    page_number=meta.get("page_number", 1),
                    document_title=meta.get("document_title", ""),
                    similarity_score=round(float(dense_sim), 4)
                )
                candidate_chunks.append((chunk, dense_sim, lexical_sim))

        if not candidate_chunks:
            return []

        # Reciprocal Rank Fusion (RRF)
        # Sort by dense
        sorted_by_dense = sorted(candidate_chunks, key=lambda x: x[1], reverse=True)
        dense_ranks = {item[0].id: rank for rank, item in enumerate(sorted_by_dense, start=1)}

        # Sort by lexical
        sorted_by_lexical = sorted(candidate_chunks, key=lambda x: x[2], reverse=True)
        lexical_ranks = {item[0].id: rank for rank, item in enumerate(sorted_by_lexical, start=1)}

        # RRF k constant = 60
        fused_scores: List[Tuple[Chunk, float]] = []
        for chunk, dense_sim, lexical_sim in candidate_chunks:
            r_dense = dense_ranks.get(chunk.id, 100)
            r_lex = lexical_ranks.get(chunk.id, 100)
            rrf_score = (1.0 / (60.0 + r_dense)) + (1.0 / (60.0 + r_lex))

            # Calibrated composite similarity score
            composite_sim = (dense_sim * 0.65) + (min(1.0, lexical_sim) * 0.35)
            # Bonus for high RRF rank
            final_sim = round(float(min(1.0, max(composite_sim, dense_sim * 0.85 + (rrf_score * 15.0)))), 4)

            if final_sim >= threshold or dense_sim >= threshold:
                chunk.similarity_score = max(final_sim, round(dense_sim, 4))
                fused_scores.append((chunk, chunk.similarity_score))

        # Sort descending by final score
        fused_scores.sort(key=lambda x: x[1], reverse=True)

        # Deduplicate identical chunk IDs if any
        seen_ids = set()
        final_chunks: List[Chunk] = []
        for c, _ in fused_scores:
            if c.id not in seen_ids:
                seen_ids.add(c.id)
                final_chunks.append(c)
            if len(final_chunks) >= k:
                break

        query_logger.info(f"Hybrid retrieval returned {len(final_chunks)} fused chunks above threshold {threshold}.")
        return final_chunks
