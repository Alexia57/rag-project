import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class DocumentRetriever:
    """Class to index and retrieve documents using FAISS."""
    
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.doc_store = {}

    def build_index(self, documents):
        """Generate embeddings and build FAISS index."""
        embeddings = self.model.encode([doc for doc in documents], convert_to_numpy=True)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

        # Store the documents
        self.doc_store = {i: doc for i, doc in enumerate(documents)}

    def retrieve(self, query, k=3):
        """Retrieve top-k relevant documents."""
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding.astype("float32"), k)

        return [(self.doc_store[i], distances[0][j]) for j, i in enumerate(indices[0])]
