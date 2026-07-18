from backend.app.memory.conversation import conversation_manager
from backend.app.services.llm import llm_service


def process_message(message: str):

    conversation_manager.add_message(
        "user",
        message
    )

    reply = llm_service.generate_response(
        message=message,
        history=conversation_manager.get_history()
    )

    conversation_manager.add_message(
        "assistant",
        reply
    )

    return {
        "assistant_reply": reply,
        "conversation": conversation_manager.get_history()
    }