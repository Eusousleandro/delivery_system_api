from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.application.use_cases.user_service import UserService
from app.interfaces.schemas.user_schema import UserResponse

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/', response_model=UserResponse)
async def get_all(
    db: Session = Depends(),
    service: UserService = Depends()
):
    return await service.get_all(db)

@router.get('/{id}', response_model=UserResponse)
async def get_user_id(
    id: int,
    db: Session = Depends(),
    service: UserService = Depends()
):
    pass

@router.post('/', response_model=UserResponse)
async def create(
    db: Session = Depends(),
    service: UserService = Depends()
):
    pass

@router.put('/{id}', response_model=UserResponse)
async def update(
    db: Session = Depends(),
    service: UserService = Depends()
):
    pass

@router.delete('/{id}', response_model=UserResponse)
async def delete(
    db: Session = Depends(),
    service: UserService = Depends()
):
    pass