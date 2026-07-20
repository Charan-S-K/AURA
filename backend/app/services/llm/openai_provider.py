from openai import OpenAI

from backend.app.config.settings import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
)

from backend.app.models.message import Message
from backend.app.prompts.system_prompt import SYSTEM_PROMPT

from .provider import LLMProvider


class OpenAIProvider(LLMProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def generate_response(
        self,
        message: str,
        history: list[Message],
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

        for item in history:

            messages.append(
                {
                    "role": item.role,
                    "content": item.content,
                }
            )

        try:

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=messages,
            )

            return response.choices[0].message.content

        except Exception as e:

            print(e)

            return (
                "Sorry, I couldn't connect to the AI service."
            )