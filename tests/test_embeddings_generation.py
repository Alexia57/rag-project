from test_model_initialization import test_model_initialization
import torch

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

# Example test with dummy chunks
#model, tokenizer = test_model_initialization("BAAI/bge-small-en")
chunks = ["This is a test chunk.", "Here is another chunk of text."]
#embeddings = test_embeddings_generation(model, tokenizer, chunks)
#print(embeddings)