from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse
from sentence_transformers import SentenceTransformer
import requests
import json

app = FastAPI()

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CONFIG ---
OLLAMA_MODEL = "llama3.2:1b"
OLLAMA_URL = "http://localhost:11434/api/generate"
PINECONE_API_KEY = "pcsk_3dtYy2_2YG7mAqcKpRhxe8TDa3Gm9jeaSwL1xHmFKNmBFpRjWWYfSbywt6ZvahAbRcj1SU"  # your API key
ASSISTANT_ID = "myrag"
PINECONE_ASSISTANT_URL = f"https://prod-1-data.ke.pinecone.io/assistant/chat/{ASSISTANT_ID}"



@app.options("/chat")
async def options_handler():
    return JSONResponse(status_code=200)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data["messages"][0]["content"]

    # Step 1: Query Pinecone Assistant
    payload = {
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    headers = {
        "Api-Key": PINECONE_API_KEY,
        "Content-Type": "application/json"
    }

    pinecone_response = requests.post(PINECONE_ASSISTANT_URL, json=payload, headers=headers)
    
    try:
        pinecone_data = pinecone_response.json()
        pinecone_context = pinecone_data.get("message", {}).get("content", "")
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": "Invalid Pinecone response", "details": pinecone_response.text}
        )

    # Step 2: Build prompt for Ollama
    prompt = f"""You are a helpful assistant. Use the context below to answer the user's question.

Context:
{pinecone_context}

User: {user_input}
Answer:"""

    # Step 3: Stream Ollama response
    def stream_response():
        response = requests.post(
            OLLAMA_URL,
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": True},
            stream=True
        )
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    if "response" in data:
                        yield f"data: {json.dumps({'type': 'content_chunk', 'delta': {'content': data['response']}})}\n\n"
                except Exception as e:
                    print("Error parsing chunk:", e, line)
        yield "data: [DONE]\n\n"

    return StreamingResponse(stream_response(), media_type="text/event-stream")
