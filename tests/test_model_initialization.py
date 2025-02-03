from transformers import AutoTokenizer, AutoModel
import torch

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

# Test with your model
#test_model_initialization("BAAI/bge-small-en")
