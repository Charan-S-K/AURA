from backend.app.brain.intent import Intent


class IntentDetector:

    def detect(self, message: str) -> Intent:

        text = message.strip().lower()

        memory_store_patterns = [

            "remember",

            "my name is",
            "i am ",
            "i'm ",

            "my college is",
            "i study at",
            "i'm studying at",

            "i work at",
            "i work for",

            "my university is",

            "i live in",
            "i'm from",
            "my hometown is",
            "my city is",

            "my favourite language is",
            "my favorite language is",

            "my birthday is",

            "i am an",
            "i'm an",

            "i am a",
            "i'm a",
        ]

        if any(pattern in text for pattern in memory_store_patterns):
            return Intent.MEMORY_STORE

        memory_recall_patterns = [

            "what is my",
            "what's my",

            "who am i",

            "where do i study",
            "where do i work",

            "where do i live",

            "what is my birthday",
            "when is my birthday",

        ]

        if any(pattern in text for pattern in memory_recall_patterns):
            return Intent.MEMORY_RECALL

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

        if any(keyword in text for keyword in scheduler_keywords):
            return Intent.SCHEDULER

        return Intent.CHAT


intent_detector = IntentDetector()