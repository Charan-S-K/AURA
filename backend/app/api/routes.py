from fastapi import APIRouter

from backend.app.models.chat import ChatRequest
from backend.app.services.assistant import process_message
from backend.app.config.settings import (
    APP_NAME,
    APP_VERSION,
    ASSISTANT_NAME,
)

router = APIRouter()


@router.get("/")
def home():
    return {
        "application": APP_NAME,
        "assistant": ASSISTANT_NAME,
        "status": "Running",
        "version": APP_VERSION
    }


@router.get("/health")
def health():
    return {
        "status": "Healthy",
    }


@router.get("/assistant")
def assistant():
    return {
        "name": ASSISTANT_NAME,
        "version": APP_VERSION,
    }


@router.post("/chat")
def chat(request: ChatRequest):
    return process_message(request.message)