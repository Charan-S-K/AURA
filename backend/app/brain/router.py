from backend.app.brain.intent import Intent


class Router:

    def route(
        self,
        intent: Intent,
    ) -> Intent:

        return intent


router = Router()