from fastapi import FastAPI

from app.infrastructure.database.connection import engine, Base
from app.interfaces.api.login_controller import router as login_router
from app.interfaces.api.user_controller import router as user_router
from app.interfaces.api.order_controller import router as order_router
from app.interfaces.websockets.order_web_controller import router as order_webs_router
from app.interfaces.handler.exceptions_handler import register_exception_handlers

app = FastAPI()
Base.metadata.create_all(bind=engine)

register_exception_handlers(app)

app.include_router(login_router)
app.include_router(user_router)
app.include_router(order_router)
app.include_router(order_webs_router)