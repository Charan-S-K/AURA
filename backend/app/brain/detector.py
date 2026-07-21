from backend.app.brain.intent import Intent


class IntentDetector:

    def detect(self, message: str) -> Intent:

        text = message.strip().lower()

        if "remember" in text:
            return Intent.MEMORY_STORE

        if "what is my name" in text or "who am i" in text:
            return Intent.MEMORY_RECALL

        if "alarm" in text or "remind" in text:
            return Intent.SCHEDULER

        return Intent.CHAT


intent_detector = IntentDetector()