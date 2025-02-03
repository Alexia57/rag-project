import os
import fitz  # PyMuPDF

class DocumentLoader:
    """Class to load and extract text from PDF and TXT files."""
    
    def __init__(self, directory="data/"):
        self.directory = directory

    def load_documents(self):
        """Load and extract text from all files in the directory."""
        documents = []
        
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)

            if filename.endswith(".txt"):
                with open(filepath, "r", encoding="utf-8") as file:
                    documents.append(file.read())

            elif filename.endswith(".pdf"):
                text = ""
                with fitz.open(filepath) as pdf:
                    for page in pdf:
                        text += page.get_text("text")
                documents.append(text)

        return documents