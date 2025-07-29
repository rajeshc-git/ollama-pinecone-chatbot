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

# 💬 Hybrid RAG Chatbot with Ollama, Pinecone & FastAPI

A lightweight, privacy-respecting chatbot built using:

- 🔗 Ollama (local LLM: llama3.2:1b)
- 🧠 Pinecone vector DB for context retrieval
- ⚡ FastAPI backend
- 🖥️ HTML frontend
- 💬 Real-time streaming response

---

## 📁 Folder Structure (suggested)

ollama-pinecone-chatbot/
├── frontend/ # HTML, JS, CSS files
│ └── index.html
├── main.py # FastAPI backend
├── requirements.txt # Python dependencies
├── README.md
├── .gitignore



---

## 🧠 How It Works

1. User sends a message from the frontend.
2. Backend queries Pinecone for relevant data.
3. Prompt is created using the context + question.
4. Ollama responds with an answer (streamed).
5. Frontend shows the live response.

---

## 🛠️ Setup Instructions

### Backend (FastAPI + Ollama)

```bash
pip install -r requirements.txt
uvicorn main:app --reload
Make sure Ollama is running:


ollama run llama3.2:1b
Edit main.py and set your Pinecone API Key and Assistant ID.

📦 Python Dependencies
Paste this in a file called requirements.txt:


fastapi
uvicorn
requests
sentence-transformers

📄 License
MIT
