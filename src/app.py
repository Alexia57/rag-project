import streamlit as st
from document_loader import DocumentLoader
from text_splitter import TextSplitter
from retriever import DocumentRetriever
from generator import ResponseGenerator

# Load and process documents
st.sidebar.title("🔍 Document RAG Chatbot")
st.sidebar.write("Loading documents...")

@st.cache_resource
def load_data():
    loader = DocumentLoader()
    documents = loader.load_documents()
    splitter = TextSplitter()
    chunks = splitter.split_documents(documents)
    retriever = DocumentRetriever()
    retriever.build_index([chunk.page_content for chunk in chunks])
    generator = ResponseGenerator()
    return retriever, generator

retriever, generator = load_data()

def chat_with_rag(question):
    retrieved_docs = retriever.retrieve(question)
    context = "\n".join([doc for doc, _ in retrieved_docs])
    
    # Display retrieved docs
    with st.expander("📄 Retrieved Documents & Scores"):
        for i, (doc, score) in enumerate(retrieved_docs):
            st.write(f"**Doc {i+1} (Score: {score:.4f})**")
            st.text_area(label="", value=doc[:500], height=100)  # Show first 500 chars
    
    return generator.generate(question, context)

# Streamlit UI
st.title("💬 RAG Chatbot")
st.write("Ask a question about your documents 📚")

# User input
user_question = st.text_input("Your question:")

if st.button("Send"):
    if user_question:
        response = chat_with_rag(user_question)
        st.markdown("### 🤖 Chatbot Response:")
        st.write(response)
    else:
        st.warning("❗ Please enter a question.")
