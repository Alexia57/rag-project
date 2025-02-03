import ollama
from string import Template


prompt_template = Template("""
Use ONLY the context below.
If unsure, say "I don't know".
Keep answers under 4 sentences.

Context: $context
Question: $question
Answer:
""")

class ResponseGenerator:
    """Class to generate responses using an LLM model."""
    
    def __init__(self, model="deepseek-r1"):
        self.model = model

    def generate(self, query, context):
        """Generate a response using the retrieved context."""
        response = ollama.chat(model="deepseek-r1:1.5b", messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": prompt_template.substitute(context=context, question=query)}
        ])
        return response["message"]["content"]

