from backend.app.prompts.system_prompt import SYSTEM_PROMPT
class LLMService:

    def generate_response(
        self,
        message: str,
        history: list,
    ) -> str:

        print("===== SYSTEM PROMPT =====")
        print(SYSTEM_PROMPT)

        return f"You said: {message}"


llm_service = LLMService()