from backend.app.memory.classifier import (
    memory_classifier,
)

from backend.app.memory.extractor import (
    memory_extractor,
)

from backend.app.repositories.memory_repository import (
    memory_repository,
)


class MemoryManager:

    # ------------------------------------------------------
    # Store memory
    # ------------------------------------------------------

    def store(
        self,
        message: str,
    ) -> str | None:

        # --------------------------------------------------
        # Step 1:
        # Try deterministic extraction first.
        # --------------------------------------------------

        result = memory_extractor.extract_store(
            message
        )

        if result is not None:

            key, value = result

            return self._save_memory(
                key=key,
                value=value,
            )

        # --------------------------------------------------
        # Step 2:
        # Use AI classification when the explicit
        # extractor doesn't recognize the message.
        # --------------------------------------------------

        classification = (
            memory_classifier.classify(
                message
            )
        )

        if not classification.remember:

            return None

        if (
            classification.key is None
            or classification.value is None
        ):

            return None

        return self._save_memory(
            key=classification.key,
            value=classification.value,
        )

    # ------------------------------------------------------
    # Recall memory
    # ------------------------------------------------------

    def recall(
        self,
        message: str,
    ) -> str:

        key = memory_extractor.extract_recall(
            message
        )

        if key is None:

            return (
                "I couldn't understand "
                "what you wanted to recall."
            )

        value = memory_repository.get(
            key
        )

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

    # ------------------------------------------------------
    # Build memory context
    # ------------------------------------------------------

    def get_context(self) -> str:

        from backend.app.memory.context_builder import (
            memory_context_builder,
        )

        return memory_context_builder.build()

    # ------------------------------------------------------
    # Save or update memory
    # ------------------------------------------------------

    def _save_memory(
        self,
        key: str,
        value: str,
    ) -> str:

        existing = memory_repository.get(
            key
        )

        # --------------------------------------------------
        # Memory already contains exactly the same value
        # --------------------------------------------------

        if existing is not None:

            if (
                existing.strip().lower()
                == value.strip().lower()
            ):

                return (
                    f"I already know your "
                    f"{key.replace('_', ' ')} "
                    f"is {value}."
                )

        # --------------------------------------------------
        # New memory or updated memory
        # --------------------------------------------------

        memory_repository.save(
            key,
            value,
        )

        return (
            f"I'll remember your "
            f"{key.replace('_', ' ')} "
            f"is {value}."
        )


memory_manager = MemoryManager()