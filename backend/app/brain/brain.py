from backend.app.brain.detector import intent_detector
from backend.app.brain.router import router
from backend.app.brain.intent import Intent


class Brain:

    def process(
        self,
        message: str,
    ) -> Intent:

        intent = intent_detector.detect(message)

        print(f"Intent : {intent.value}")

        return router.route(intent)


brain = Brain()