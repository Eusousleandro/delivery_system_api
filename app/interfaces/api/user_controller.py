from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.application.use_cases.user_service import UserService
from app.infrastructure.security.auth_service import AuthService
from app.interfaces.dependencies.user_dependency import get_user_service
from app.interfaces.schemas.user_schema import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/', response_model=List[UserResponse])
async def get_all(
    current_user = Depends(AuthService.get_current_user),
    service: UserService = Depends(get_user_service)
):
    return await service.get_all()

@router.get('/{id}', response_model=UserResponse)
async def get_user_id(
    id: int,
    current_user = Depends(AuthService.get_current_user),
    service: UserService = Depends(get_user_service)
):
    return await service.get_user_id(id=id)

@router.post('/', response_model=UserResponse)
async def create(
    user: UserCreate = Depends(),
    current_user = Depends(AuthService.get_current_user), 
    service: UserService = Depends(get_user_service)
):
    return await service.create(user)

@router.put('/{id}', response_model=UserResponse)
async def update(
    user: UserUpdate = Depends(),
    current_user = Depends(AuthService.get_current_user),
    service: UserService = Depends(get_user_service)
):
    return await service.update(id, user)

@router.delete('/{id}', response_model=UserResponse)
async def delete(
    id: int,
    current_user = Depends(AuthService.get_current_user),
    service: UserService = Depends(get_user_service)
):
    return await service.delete(id)