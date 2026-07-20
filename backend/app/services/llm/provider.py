from abc import ABC, abstractmethod

from backend.app.models.message import Message


class LLMProvider(ABC):

    @abstractmethod
    def generate_response(
        self,
        message: str,
        history: list[Message],
    ) -> str:
        pass