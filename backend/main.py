from fastapi import FastAPI

from app.api.routes import router
from app.config.settings import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Artificial Universal Responsive Assistant",
)

app.include_router(router)