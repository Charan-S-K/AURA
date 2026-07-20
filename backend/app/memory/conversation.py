from backend.app.models.message import Message
from backend.app.services.database_service import database_service
from backend.app.config.settings import MAX_CONTEXT_MESSAGES

class ConversationManager:

    def __init__(self):
        self.history: list[Message] = []
        self.load_previous_messages()

    def load_previous_messages(self):

        self.history.clear()

        messages = database_service.load_messages()

        for message in messages:

            self.history.append(
                Message(
                    role=message.role,
                    content=message.content
                )
            )

    def get_recent_history(
        self,
        limit: int = MAX_CONTEXT_MESSAGES,
    ) -> list[Message]:

        return self.history[-limit:]

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