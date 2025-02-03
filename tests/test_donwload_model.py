from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "meta-llama/Llama-2-7b-chat-hf"  # Nom du modèle sur Hugging Face
local_path = "./models/llama-2-7b-chat"  # Chemin local où enregistrer le modèle

# Téléchargement
print(f"🔄 Downloading {model_name}...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Sauvegarde locale
print(f"💾 Saving model to {local_path}...")
tokenizer.save_pretrained(local_path)
model.save_pretrained(local_path)
print("✅ Model saved locally!")
