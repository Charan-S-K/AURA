from fastapi import FastAPI
from backend.app.database import database

from backend.app.api.routes import router
from backend.app.config.settings import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Artificial Universal Responsive Assistant",
)

app.include_router(router)