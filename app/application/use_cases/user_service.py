from typing import List
from sqlalchemy.orm import Session

from app.domain.exceptions.exception import  AlreadyExistsException, CouldNotBeCreated, CreatedonFailedException, DeletionFailedException, NotFoundException, UpdatedonFailedException
from app.infrastructure.repositories.user_repository_implementation import UserRepository
from app.infrastructure.security.jwt_service import AuthService
from app.interfaces.mappers.user_mapper import to_user_response
from app.interfaces.schemas.user_schema import UserCreate, UserUpdate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_all(self) -> List[dict]:
        users = await self.repository.get_all()
        if not users:
            return []
        
        return [to_user_response(u) for u in users]

    async def get_user_id(self, id: int) -> dict:
        user = await self.repository.get_user_id(id)
        if not user:
            raise NotFoundException()
        return to_user_response(user)

    async def create(self, user: UserCreate) -> dict:
        user = await self.repository.get_user_email(user.email)
        if user:
            raise AlreadyExistsException()
        
        user.password = AuthService.hash_password(user.password)
        created = await self.repository.create(user)
        if not created:
            raise CreatedonFailedException()
        
        return created
    
    async def update(self, id: int, user: UserUpdate) -> dict:
        user = await self.repository.get_user_id(id)
        if not user:
            raise NotFoundException()
        
        sucess = await self.repository.update(user)
        if not sucess:
            raise UpdatedonFailedException()
        return sucess
    
    async def delete(self, id: int) -> None:
        user = await self.repository.get_user_id(id)
        if not user:
            raise NotFoundException()
        
        sucess = await self.repository.delete(id)
        if not sucess:
            raise DeletionFailedException()
        return sucess