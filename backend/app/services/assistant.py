from app.memory.conversation import conversation_manager


def process_message(message: str):

    conversation_manager.add_message(
        "user",
        message
    )

    reply = f"You said: {message}"

    conversation_manager.add_message(
        "assistant",
        reply
    )

    return {
        "assistant_reply": reply,
        "conversation": conversation_manager.get_history()
    }