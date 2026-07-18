from backend.app.models.message import Message
from backend.app.services.database_service import database_service

class ConversationManager:

    def __init__(self):
        self.history: list[Message] = []

    def add_message(self, role: str, content: str):

        message = Message(
            role=role,
            content=content
        )

        self.history.append(message)

        database_service.save_message(
            role,
            content
        )

    def get_history(self) -> list[Message]:
        return self.history.copy()

    def clear_history(self):

        self.history.clear()


conversation_manager = ConversationManager()