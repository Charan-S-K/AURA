from backend.app.brain.intent import Intent


class Router:

    def route(
        self,
        intent: Intent,
    ) -> str:

        if intent == Intent.CHAT:
            return "chat"

        if intent == Intent.MEMORY_STORE:
            return "memory"

        if intent == Intent.MEMORY_RECALL:
            return "memory"

        if intent == Intent.SCHEDULER:
            return "scheduler"

        if intent == Intent.TOOL:
            return "tool"

        return "unknown"


router = Router()