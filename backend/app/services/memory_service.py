from backend.app.memory.conversation import conversation_manager


class MemoryService:

    def store(self, message: str) -> str:
        """
        Placeholder implementation.

        Stage 5.5 stores important information
        using the existing conversation manager.
        """

        return "I will remember that."

    def recall(self, message: str) -> str:
        """
        Placeholder implementation.

        The real implementation will search
        long-term memory in the next step.
        """

        return "I don't remember that yet."


memory_service = MemoryService()