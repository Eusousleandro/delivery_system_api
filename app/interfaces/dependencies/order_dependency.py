from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.use_cases.order_service import OrderService
from app.config.dependency_db import Dependencies
from app.infrastructure.repositories.order_repository_implementation import OrderRepository

def get_order_service(db: Session = Depends(Dependencies.get_db)) -> OrderService:
    repository = OrderRepository(db)
    return OrderService(repository)