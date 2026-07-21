from backend.app.memory.extractor import memory_extractor
from backend.app.repositories.memory_repository import memory_repository


class MemoryService:

    def store(
        self,
        message: str,
    ) -> str:

        result = memory_extractor.extract_store(message)

        if result is None:

            return "I couldn't understand what to remember."

        key, value = result

        memory_repository.save(
            key,
            value,
        )

        return (
            f"I'll remember your "
            f"{key.replace('_', ' ')} is "
            f"{value}."
        )

    def recall(
        self,
        message: str,
    ) -> str:

        key = memory_extractor.extract_recall(message)

        if key is None:

            return (
                "I couldn't understand "
                "what you wanted to recall."
            )

        value = memory_repository.get(key)

        if value is None:

            return (
                f"I don't know your "
                f"{key.replace('_', ' ')} yet."
            )

        return (
            f"Your "
            f"{key.replace('_', ' ')} "
            f"is {value}."
        )


memory_service = MemoryService()