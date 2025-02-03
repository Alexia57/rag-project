# 🧠 RAG Chatbot - Retrieval-Augmented Generation

A chatbot leveraging RAG (Retrieval-Augmented Generation) to answer questions based on documents (PDF, TXT, etc.).
Currently using FAISS for vector search, with plans to support Qdrant and other vector DBs.

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Alexia57/rag-project.git
cd rag-project
```

### 2️⃣ Set Up Environment Variables

- Copy the default environment file  to `.env` if it doesn't exist:

    ```bash
    cp default.env .env
    ```

- Update .env with your configuration.

## 🛠️ Run the Web App (With/Without Docker)

### ▶️ Option 1: Webapp & FAISS Vector Database Without Docker

1. **Create and activate the Conda environment**  

    ```bash
    conda env create -v -f environment.yml --force
    conda activate rag_project
    ```

2. **Install project dependencies with Poetry**  

    ```bash
    poetry install --without dev
    ```

3. **Run the Webapp**  

    ```bash
    streamlit run src/app.py
    ```

    By default, the application uses **FAISS** as the vector database.

4. **Access the Application**  

    Open your web browser and navigate to http://localhost:<PORT_WEBAPP> (the port you specified in the .env file).

---

### ▶️ Option 2: Not finished yet
