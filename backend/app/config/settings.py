import os
from pathlib import Path

from dotenv import load_dotenv

# Find the project root (AURA/)
BASE_DIR = Path(__file__).resolve().parents[3]

# Load AURA/.env
load_dotenv(BASE_DIR / ".env")

APP_NAME = os.getenv("APP_NAME", "AURA")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "AURA")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "mock"
)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///aura.db")
OPENAI_MODEL = os.getenv("OPENAI_MODEL","gpt-5")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)
MAX_CONTEXT_MESSAGES = int(
    os.getenv(
        "MAX_CONTEXT_MESSAGES",
        "20"
    )
)