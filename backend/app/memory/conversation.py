from backend.app.models.message import Message


class ConversationManager:

    def __init__(self):
        self.history: list[Message] = []

    def add_message(self, role: str, content: str):

        message = Message(
            role=role,
            content=content
        )

        self.history.append(message)

    def get_history(self) -> list[Message]:
        return self.history.copy()

    def clear_history(self):

        self.history.clear()


conversation_manager = ConversationManager()