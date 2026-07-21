from .mock_provider import MockProvider
from backend.app.models.message import Message
from .openai_provider import OpenAIProvider
from backend.app.config.settings import LLM_PROVIDER
from .gemini_provider import GeminiProvider

class LLMService:

    def __init__(self):
        print("Current Provider:", LLM_PROVIDER)

        if LLM_PROVIDER == "gemini":

            self.provider = GeminiProvider()

        elif LLM_PROVIDER == "openai":

            self.provider = OpenAIProvider()

        elif LLM_PROVIDER == "mock":

            self.provider = MockProvider()

        elif LLM_PROVIDER == "ollama":

            raise NotImplementedError(
                "Ollama provider will be added later."
            )

        else:

            raise ValueError(
                f"Unsupported provider: {LLM_PROVIDER}"
            )


    def generate_response(
        self,
        message: str,
        history: list[Message],
    ) -> str:

        return self.provider.generate_response(
            message,
            history,
        )


llm_service = LLMService()