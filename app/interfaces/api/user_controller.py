from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.application.use_cases.user_service import UserService
from app.config.dependency_db import Dependencies
from app.infrastructure.security.auth_service import AuthService
from app.interfaces.schemas.user_schema import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/', response_model=UserResponse)
async def get_all(
    db: Session = Depends(Dependencies.get_db),
    current_user = Depends(AuthService.get_current_user),
    service: UserService = Depends()
):
    return await service.get_all(db)

@router.get('/{id}', response_model=UserResponse)
async def get_user_id(
    id: int,
    db: Session = Depends(Dependencies.get_db),
    current_user = Depends(AuthService.get_current_user),
    service: UserService = Depends()
):
    return await service.get_user_id(db=db, id=id)

@router.post('/', response_model=UserResponse)
async def create(
    db: Session = Depends(Dependencies.get_db),
    user: UserCreate = Depends(),
    current_user = Depends(AuthService.get_current_user), 
    service: UserService = Depends()
):
    return await service.create(db=db, user=user)

@router.put('/{id}', response_model=UserResponse)
async def update(
    id: int,
    db: Session = Depends(Dependencies.get_db),
    user: UserUpdate = Depends(),
    current_user = Depends(AuthService.get_current_user),
    service: UserService = Depends()
):
    return await service.update(db=db, id=id, user=user)

@router.delete('/{id}', response_model=UserResponse)
async def delete(
    id: int,
    db: Session = Depends(Dependencies.get_db),
    current_user = Depends(AuthService.get_current_user),
    service: UserService = Depends()
):
    return await service.delete(db=db, id=id)