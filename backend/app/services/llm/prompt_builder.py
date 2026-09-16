from backend.app.memory.context_builder import memory_context_builder
from backend.app.models.message import Message
from backend.app.prompts.system_prompt import SYSTEM_PROMPT


class PromptBuilder:

    def build(
        self,
        history: list[Message],
        message: str,
    ) -> str:

        prompt = SYSTEM_PROMPT.strip()

        memory_context = memory_context_builder.build()

        if memory_context:

            prompt += "\n\n"
            prompt += memory_context

        if history:

            prompt += "\n\nConversation History:\n"

            for item in history:

                prompt += (
                    f"{item.role}: "
                    f"{item.content}\n"
                )

        prompt += (
            "\nCurrent User Message:\n"
            f"user: {message}\n"
            "assistant:"
        )

        return prompt


prompt_builder = PromptBuilder()