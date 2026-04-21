from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.use_cases.user_service import UserService
from app.config.dependency_db import Dependencies
from app.infrastructure.repositories.user_repository_implementation import UserRepository


def get_user_service(db: Session = Depends(Dependencies.get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)