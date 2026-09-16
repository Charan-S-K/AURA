from backend.app.memory.formatter import (
    memory_formatter,
)
from backend.app.memory.search import (
    memory_search,
)


class MemoryContextBuilder:

    def build(self) -> str:

        memories = memory_search.get_all()

        if not memories:
            return ""

        formatted = (
            memory_formatter.format_memories(
                memories
            )
        )

        return (
            "Known User Facts:\n"
            "-----------------\n"
            f"{formatted}"
        )


memory_context_builder = MemoryContextBuilder()