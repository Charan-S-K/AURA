from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.config.settings import DATABASE_URL
from backend.app.database.base import Base

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

# Import database models
import backend.app.database.models

# Create all tables
Base.metadata.create_all(bind=engine)