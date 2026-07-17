from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AURA API",
    version="0.1.0")

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "assistant": "AURA",
        "status": "Running"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "user_message": request.message,
        "assistant_reply": f"You said: {request.message}"
    }