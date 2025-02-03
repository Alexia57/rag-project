from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextSplitter:
    """Class to split text into chunks for processing."""

    def __init__(self, chunk_size=500, chunk_overlap=50):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    def split_documents(self, documents):
        """Split the loaded documents into smaller chunks."""
        return self.splitter.create_documents(documents)
