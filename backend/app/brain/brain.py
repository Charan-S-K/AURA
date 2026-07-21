from backend.app.brain.detector import intent_detector
from backend.app.brain.router import router


class Brain:

    def process(
        self,
        message: str,
    ) -> str:

        intent = intent_detector.detect(message)

        destination = router.route(intent)

        print(f"Intent: {intent.value}")

        print(f"Route : {destination}")

        return destination


brain = Brain()