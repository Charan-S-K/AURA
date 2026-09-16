from backend.app.brain.intent import Intent


class IntentDetector:

    def detect(self, message: str) -> Intent:

        text = message.strip().lower()

        # --------------------------------------------------
        # MEMORY STORE
        # --------------------------------------------------

        memory_store_patterns = [

            "remember",

            "my name is",
            "my nickname is",

            "my college is",
            "i study at",
            "i'm studying at",

            "my university is",

            "i work at",
            "i work for",

            "i live in",
            "i'm from",
            "my hometown is",
            "my city is",

            "my birthday is",

            "my favourite language is",
            "my favorite language is",

            "my favourite food is",
            "my favorite food is",

            "my favourite color is",
            "my favorite color is",

            "i am an",
            "i'm an",

            "i am a",
            "i'm a",
        ]

        if any(
            pattern in text
            for pattern in memory_store_patterns
        ):
            return Intent.MEMORY_STORE

        # --------------------------------------------------
        # MEMORY RECALL
        # --------------------------------------------------

        memory_recall_patterns = [

            "what is my",
            "what's my",

            "tell me my",

            "who am i",

            "where do i study",
            "where do i work",
            "where do i live",

            "what color do i like",
            "what colour do i like",

            "what food do i like",

            "what language do i like",

            "when is my birthday",
        ]

        if any(
            pattern in text
            for pattern in memory_recall_patterns
        ):
            return Intent.MEMORY_RECALL

        # --------------------------------------------------
        # SCHEDULER
        # --------------------------------------------------

        scheduler_keywords = [

            "alarm",
            "remind",
            "schedule",
            "meeting",
            "appointment",
            "calendar",
            "tomorrow",
            "today",
        ]

        if any(
            keyword in text
            for keyword in scheduler_keywords
        ):
            return Intent.SCHEDULER

        # --------------------------------------------------
        # DEFAULT CHAT
        # --------------------------------------------------

        return Intent.CHAT


intent_detector = IntentDetector()