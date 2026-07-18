from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import DATABASE_URL

# Create the SQLite engine
engine = create_engine(
    DATABASE_URL,
    echo=True,
)

# Factory for database sessions
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)