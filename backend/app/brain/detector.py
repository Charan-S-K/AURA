from backend.app.brain.intent import Intent


class IntentDetector:

    def detect(self, message: str) -> Intent:

        text = message.strip().lower()

        if "remember" in text:
            return Intent.MEMORY_STORE

        if (
            "what is my" in text
            or "what's my" in text
            or "who am i" in text
        ):
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