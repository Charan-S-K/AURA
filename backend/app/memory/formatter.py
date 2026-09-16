class MemoryFormatter:

    def format_memory(
        self,
        key: str,
        value: str,
    ) -> str:

        label = key.replace(
            "_",
            " ",
        ).title()

        return f"{label}: {value}"

    def format_memories(
        self,
        memories,
    ) -> str:

        if not memories:

            return ""

        lines = []

        for memory in memories:

            lines.append(
                self.format_memory(
                    memory.key,
                    memory.value,
                )
            )

        return "\n".join(lines)


memory_formatter = MemoryFormatter()