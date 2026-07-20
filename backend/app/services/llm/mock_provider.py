from backend.app.models.message import Message
from backend.app.prompts.system_prompt import SYSTEM_PROMPT

from .provider import LLMProvider


class MockProvider(LLMProvider):

    def generate_response(
        self,
        message: str,
        history: list[Message],
    ) -> str:

        print("===== SYSTEM PROMPT =====")
        print(SYSTEM_PROMPT)

        return f"You said: {message}"