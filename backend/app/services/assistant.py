from backend.app.brain.brain import brain
from backend.app.brain.intent import Intent

from backend.app.memory.conversation import conversation_manager
from backend.app.services.llm.llm import llm_service
from backend.app.memory.manager import memory_manager


def process_message(message: str):

    conversation_manager.add_message(
        "user",
        message,
    )

    intent = brain.process(message)

    if intent == Intent.CHAT:

        reply = llm_service.generate_response(
            message=message,
            history=conversation_manager.get_recent_history(),
        )

    elif intent == Intent.MEMORY_STORE:

        reply = memory_manager.store(message)

        if reply is None:

            reply = llm_service.generate_response(
                message=message,
                history=conversation_manager.get_recent_history(),
            )

    elif intent == Intent.MEMORY_RECALL:

        reply = memory_manager.recall(message)

    elif intent == Intent.SCHEDULER:

        reply = (
            "Scheduler routing "
            "will be implemented soon."
        )

    elif intent == Intent.TOOL:

        reply = (
            "Tool routing "
            "will be implemented soon."
        )

    else:

        reply = (
            "I couldn't determine "
            "how to process your request."
        )

    conversation_manager.add_message(
        "assistant",
        reply,
    )

    return {
        "assistant_reply": reply,
        "conversation": conversation_manager.get_history(),
    }