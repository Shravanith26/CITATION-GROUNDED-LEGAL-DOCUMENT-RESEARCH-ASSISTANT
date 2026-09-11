import numpy as np
from typing import List
from app.config.config import settings
from app.utils.logging import indexing_logger

class EmbeddingService:
    """
    Unified text embedding service.
    Uses SentenceTransformers when available, with a deterministic TF-IDF dense
    vector fallback using scikit-learn for lightweight environments.
    """
    _instance = None

    def __init__(self):
        self.model_name = settings.EMBEDDING_MODEL_NAME
        self.model = None
        self.use_fallback = False
        self._init_model()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = EmbeddingService()
        return cls._instance

    def _init_model(self):
        try:
            from sentence_transformers import SentenceTransformer
            indexing_logger.info(f"Loading SentenceTransformer model: {self.model_name}")
            self.model = SentenceTransformer(self.model_name)
            self.dimension = self.model.get_sentence_embedding_dimension()
            indexing_logger.info(f"SentenceTransformer loaded successfully. Dimension: {self.dimension}")
        except Exception as e:
            indexing_logger.warning(
                f"SentenceTransformer unavailable ({str(e)}). Initializing Scikit-Learn TF-IDF semantic vector fallback."
            )
            self.use_fallback = True
            from sklearn.feature_extraction.text import TfidfVectorizer
            self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=384)
            self.dimension = 384
            # Pre-fit on legal vocabulary seeds so transform works immediately
            seed_corpus = [
                "anticipatory bail non bailable arrest session court high court section 438 crpc bnss",
                "personal liberty article 21 constitution interrogation condition police custody",
                "charge sheet investigation witness tampering flight risk offence gravity antecedents",
                "judgment supreme court precedent magistrate summons notice section 41 41a",
                "economic offences dowry prohibition harassment marital discord guidelines"
            ]
            self.vectorizer.fit(seed_corpus)

    def embed_text(self, text: str) -> List[float]:
        """Generate embedding vector for a single text."""
        return self.embed_batch([text])[0]

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate normalized embedding vectors for a batch of texts."""
        if not texts:
            return []

        if not self.use_fallback and self.model is not None:
            embeddings = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
            return embeddings.tolist()
        else:
            # TF-IDF Fallback with dense zero-padding to dimension
            tfidf_mat = self.vectorizer.transform(texts).toarray()
            dense_list = []
            for row in tfidf_mat:
                vec = np.zeros(self.dimension, dtype=np.float32)
                vec[:len(row)] = row
                norm = np.linalg.norm(vec)
                if norm > 0:
                    vec = vec / norm
                dense_list.append(vec.tolist())
            return dense_list

    def update_fallback_vocabulary(self, corpus: List[str]):
        """Refines the TF-IDF vocabulary when documents are indexed in fallback mode."""
        if self.use_fallback and corpus:
            try:
                self.vectorizer.fit(corpus)
            except Exception as e:
                indexing_logger.error(f"Failed to update fallback vocabulary: {e}")
