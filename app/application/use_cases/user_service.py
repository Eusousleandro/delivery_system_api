from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.infrastructure.repositories.user_repository_implementation import UserRepository
from app.interfaces.mappers.user_mapper import to_user_response
from app.interfaces.schemas.user_schema import UserCreate, UserUpdate


class UserService:
    def __init__(self, repository: UserRepository = Depends()):
        self.repository = repository

    async def get_all(self, db: Session):
        users = await self.repository.get_all(db)
        if not users:
            raise HTTPException('Users not found')
        return [to_user_response(u) for u in users]

    async def get_user_id(self, db: Session, id: int):
        user = await self.repository.get_user_id(db, id=id)
        if not user:
            raise HTTPException(status_code=401, detail='User not found')
        return to_user_response(user)

    async def create(self, db: Session, user: UserCreate):
        user_existing = await self.repository.get_user_id(db, email=user.email)
        if user_existing:
            raise HTTPException(status_code=400, detail='We were unable to create the user; the email address is already registered.')
        
        new_user = await self.repository.create(db, user=user)
        if not new_user:
            raise HTTPException(status_code=404, detail='User could not be created')
        
        return new_user
    
    async def update(self, db: Session, id: int, user: UserUpdate):
        user_existing = await self.repository.get_user_id(db, id=id)
        if not user_existing:
            raise HTTPException(status_code=401, detail='User not found')
        
        user_update = await self.repository.update(db, user=user)
        if not user_update:
            raise HTTPException(status_code=404, detail='The user could not be updated.')

    async def delete(self, db: Session, id: int):
        user_existing = await self.repository.get_user_id(db, id=id)
        if not user_existing:
            raise HTTPException(status_code=401, detail='User not found')
        
        delete_user = await self.repository.delete(db, id=id)
        if not delete_user:
            raise HTTPException(status_code=404, detail='The user could not be deleted.')

        return delete_user