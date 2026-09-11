from typing import List
from app.models.chunk import Chunk
from app.nlp.embeddings import EmbeddingService
from app.utils.logging import indexing_logger

class EmbeddingServiceImpl:
    """
    Coordinates embedding generation for documents and query vectors.
    """
    def __init__(self):
        self.embedding_provider = EmbeddingService.get_instance()

    def generate_chunk_embeddings(self, chunks: List[Chunk]) -> List[List[float]]:
        """Generates embedding vectors for a list of chunks."""
        if not chunks:
            return []
        texts = [chunk.text for chunk in chunks]
        embeddings = self.embedding_provider.embed_batch(texts)
        indexing_logger.info(f"Generated {len(embeddings)} embeddings.")
        return embeddings

    def generate_query_embedding(self, query_text: str) -> List[float]:
        """Generates embedding vector for a single query text."""
        return self.embedding_provider.embed_text(query_text)
