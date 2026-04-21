from fastapi import FastAPI

from app.interfaces.api.user_controller import router as user_router
from app.interfaces.handler.exceptions_handler import register_exception_handlers

app = FastAPI()

register_exception_handlers(app)
app.include_router(user_router)