from sqlalchemy.orm import Session

from backend.app.database.database import SessionLocal
from backend.app.models.memory import Memory


class MemoryRepository:

    def save(
        self,
        key: str,
        value: str,
    ) -> None:

        db: Session = SessionLocal()

        try:

            memory = (
                db.query(Memory)
                .filter(Memory.key == key)
                .first()
            )

            if memory:

                memory.value = value

            else:

                memory = Memory(
                    key=key,
                    value=value,
                )

                db.add(memory)

            db.commit()

        finally:

            db.close()

    def get(
        self,
        key: str,
    ) -> str | None:

        db: Session = SessionLocal()

        try:

            memory = (
                db.query(Memory)
                .filter(Memory.key == key)
                .first()
            )

            if memory:

                return memory.value

            return None

        finally:

            db.close()

    def get_all(self) -> list[Memory]:

        db: Session = SessionLocal()

        try:

            return (
                db.query(Memory)
                .order_by(Memory.key.asc())
                .all()
            )

        finally:

            db.close()

    def delete(
        self,
        key: str,
    ) -> bool:

        db: Session = SessionLocal()

        try:

            memory = (
                db.query(Memory)
                .filter(Memory.key == key)
                .first()
            )

            if memory is None:

                return False

            db.delete(memory)

            db.commit()

            return True

        finally:

            db.close()


memory_repository = MemoryRepository()