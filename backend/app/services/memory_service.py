from backend.app.memory.manager import (
    memory_manager,
)


class MemoryService:

    def store(
        self,
        message: str,
    ) -> str:

        result = memory_manager.store(
            message
        )

        if result is None:

            return (
                "I couldn't identify any "
                "personal information to remember."
            )

        return result

    def recall(
        self,
        message: str,
    ) -> str:

        return memory_manager.recall(
            message
        )


memory_service = MemoryService()