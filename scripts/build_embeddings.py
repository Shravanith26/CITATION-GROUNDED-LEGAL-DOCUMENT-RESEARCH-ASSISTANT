import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(os.path.dirname(current_dir), "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.nlp.embeddings import EmbeddingService

def test_embeddings():
    print("Initializing embedding model...")
    service = EmbeddingService.get_instance()
    sample_text = "Section 438 of the Code of Criminal Procedure provides direction for grant of anticipatory bail."
    vec = service.embed_text(sample_text)
    print(f"Embedding generated successfully!")
    print(f"Dimension: {len(vec)}")
    print(f"Sample vector snippet: {vec[:5]}...")

if __name__ == "__main__":
    test_embeddings()
