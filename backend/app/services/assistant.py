from backend.app.memory.conversation import conversation_manager
from backend.app.services.llm.llm import llm_service
from backend.app.brain.brain import brain
from backend.app.services.memory_service import memory_service


def process_message(message: str):

    conversation_manager.add_message(
        "user",
        message
    )
    destination = brain.process(message)

    if destination == "chat":

        reply = llm_service.generate_response(
            message=message,
            history=conversation_manager.get_recent_history()
        )

    elif destination == "memory":

        if "remember" in message.lower():

            reply = memory_service.store(message)

        else:

            reply = memory_service.recall(message)

    else:

        reply = (
            f"{destination} routing "
            "will be implemented soon."
        )

    conversation_manager.add_message(
        "assistant",
        reply
    )

    return {
        "assistant_reply": reply,
        "conversation": conversation_manager.get_history()
    }