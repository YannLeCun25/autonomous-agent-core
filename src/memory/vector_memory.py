import numpy as np
from typing import List, Tuple

class SemanticMemory:
    """Long-term vector memory for agents using cosine similarity."""
    def __init__(self, embedding_dim: int = 1536):
        self.storage = []
        self.embeddings = []

    def commit(self, text: str, vector: np.ndarray):
        self.storage.append(text)
        self.embeddings.append(vector)

    def query(self, query_vector: np.ndarray, top_k: int = 3) -> List[Tuple[str, float]]:
        """Retrieve top-k relevant memories."""
        if not self.embeddings: return []
        sims = np.dot(self.embeddings, query_vector) / (np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_vector))
        indices = np.argsort(sims)[-top_k:][::-1]
        return [(self.storage[i], sims[i]) for i in indices]
