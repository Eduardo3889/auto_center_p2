from fastapi import FastAPI

from app.interfaces.api import router


app = FastAPI(
    title="Auto Center Marica - Notification Service",
    version="1.0.0",
)
app.include_router(router)

