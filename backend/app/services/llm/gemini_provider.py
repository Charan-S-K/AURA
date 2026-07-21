from google import genai

from backend.app.config.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)

from backend.app.models.message import Message
from backend.app.prompts.system_prompt import SYSTEM_PROMPT

from .provider import LLMProvider


class GeminiProvider(LLMProvider):

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate_response(
        self,
        message: str,
        history: list[Message],
    ) -> str:
        print("===== GEMINI PROVIDER =====")
        prompt = SYSTEM_PROMPT + "\n\n"

        for item in history:
            prompt += f"{item.role}: {item.content}\n"

        prompt += f"user: {message}\nassistant:"

        try:

            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )

            return response.text

        except Exception as e:

            print(f"Gemini Error: {e}")

            return "Sorry, I couldn't connect to Gemini."