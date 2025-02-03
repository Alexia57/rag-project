from transformers import AutoTokenizer, AutoModel
import torch
import faiss
import numpy as np

# Étape 1 : Initialisation du modèle
def test_model_initialization(model_name: str, device: str = "cpu"):
    try:
        print(f"🔄 Initializing model: {model_name} on {device}")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name).to(device)
        print("✅ Model and tokenizer loaded successfully!")
        return model, tokenizer
    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        return None, None

# Étape 2 : Génération des embeddings
def test_embeddings_generation(model, tokenizer, chunks, device="cpu"):
    try:
        print("🔄 Generating embeddings for text chunks...")
        embeddings = []
        for chunk in chunks:
            inputs = tokenizer(chunk, return_tensors="pt", truncation=True, max_length=512).to(device)
            with torch.no_grad():
                outputs = model(**inputs)
            embeddings.append(outputs.last_hidden_state.mean(dim=1))  # Moyenne des embeddings
        print(f"✅ Generated embeddings for {len(embeddings)} chunks!")
        return embeddings
    except Exception as e:
        print(f"❌ Failed to generate embeddings: {e}")
        return []

# Étape 3 : Indexation avec FAISS
def test_faiss_index(embeddings):
    try:
        print("🔄 Creating FAISS index...")
        dimension = embeddings[0].shape[-1]
        index = faiss.IndexFlatL2(dimension)  # Index pour L2 (cosine distance)
        index.add(np.vstack([e.cpu().numpy() for e in embeddings]))  # Ajoute les embeddings
        print(f"✅ FAISS index created with {index.ntotal} vectors!")

        # Test de recherche
        query_vector = embeddings[0].cpu().numpy().reshape(-1, dimension)  # Assure une matrice 2D
        print(f"Shape of query_vector for search: {query_vector.shape}")

        distances, indices = index.search(query_vector, k=3)
        print(f"Distances: {distances}")
        print(f"Indices: {indices}")
    except Exception as e:
        print(f"❌ Failed to create FAISS index: {e}")



# Étape 4 : Exemple d'utilisation
if __name__ == "__main__":
    model_name = "BAAI/bge-small-en"
    chunks = ["This is a test chunk.", "Here is another chunk of text.", "You know the concept."]
    device = "cpu"  # Ou "cuda" si GPU disponible

    # Initialisation
    model, tokenizer = test_model_initialization(model_name, device)
    if model is not None and tokenizer is not None:
        # Génération des embeddings
        embeddings = test_embeddings_generation(model, tokenizer, chunks, device)

        # Indexation et recherche avec FAISS
        if embeddings:
            test_faiss_index(embeddings)
