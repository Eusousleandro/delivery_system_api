from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.use_cases.authenticate_sercive import AuthentService
from app.config.dependency_db import Dependencies
from app.infrastructure.repositories.user_repository_implementation import UserRepository


def get_auth_service(db: Session = Depends(Dependencies.get_db)) -> AuthentService:
    repository = UserRepository(db)
    return AuthentService(repository)