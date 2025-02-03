import gradio as gr
from document_loader import DocumentLoader
from text_splitter import TextSplitter
from retriever import DocumentRetriever
from generator import ResponseGenerator

# Load and process documents
loader = DocumentLoader()
documents = loader.load_documents()

splitter = TextSplitter()
chunks = splitter.split_documents(documents)

retriever = DocumentRetriever()
retriever.build_index([chunk.page_content for chunk in chunks])

generator = ResponseGenerator()

def chat_with_rag(question):
    retrieved_docs = retriever.retrieve(question)
    context = "\n".join([doc for doc, _ in retrieved_docs])
    return generator.generate(question, context)

# Launch Gradio UI
gr.Interface(
    fn=chat_with_rag, 
    inputs="text", 
    outputs="text", 
    title="Chatbot RAG",
    description="Ask your chatbot a question about your documents."
).launch()
