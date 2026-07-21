from sqlalchemy import Column, Integer, String

from backend.app.database.database import Base


class Memory(Base):

    __tablename__ = "memory"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    key = Column(
        String,
        unique=True,
        nullable=False
    )

    value = Column(
        String,
        nullable=False
    )