from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class MessageTable(Base):

    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    role: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )