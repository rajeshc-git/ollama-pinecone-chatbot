# 💬 Hybrid RAG Chatbot with Ollama, Pinecone & FastAPI

This project demonstrates a fully local chatbot with Retrieval-Augmented Generation (RAG) capabilities using:

- 🔗 [Ollama](https://ollama.com/) for running LLMs like `llama3.2:1b` locally
- 🧠 [Pinecone](https://www.pinecone.io/) for vector search and context retrieval
- ⚡ FastAPI backend with real-time streaming
- 🖥️ HTML frontend for user interaction

---

## 🧠 How It Works

1. User enters a message in the frontend.
2. Message is sent to the FastAPI `/chat` endpoint.
3. Pinecone returns relevant context.
4. Ollama is prompted with context + question.
5. Streaming response is shown to the user.

---

## 🛠️ Setup Instructions

### Backend (FastAPI + Ollama)

```bash
pip install -r requirements.txt
uvicorn main:app --reload
