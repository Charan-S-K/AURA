from backend.app.repositories.memory_repository import (
    memory_repository,
)


class MemorySearch:

    def get(self, key: str) -> str | None:

        return memory_repository.get(key)

    def get_all(self):

        return memory_repository.get_all()

    def contains(self, key: str) -> bool:

        return (
            memory_repository.get(key)
            is not None
        )


memory_search = MemorySearch()