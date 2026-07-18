from sqlalchemy.orm import Session

from backend.app.database.database import SessionLocal
from backend.app.database.models import MessageTable


class DatabaseService:

    def save_message(self, role: str, content: str):

        db: Session = SessionLocal()

        try:

            message = MessageTable(
                role=role,
                content=content,
            )

            db.add(message)

            db.commit()

        finally:

            db.close()

    def load_messages(self):

        db: Session = SessionLocal()

        try:

            messages = db.query(MessageTable).order_by(
                MessageTable.id
            ).all()

            return messages

        finally:

            db.close()


database_service = DatabaseService()