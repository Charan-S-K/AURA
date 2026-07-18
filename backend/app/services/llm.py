class LLMService:

    def generate_response(
        self,
        message: str,
        history: list
    ) -> str:

        return f"You said: {message}"


llm_service = LLMService()