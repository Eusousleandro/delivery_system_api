from typing import List

from fastapi import APIRouter, Depends

from app.application.use_cases.order_service import OrderService
from app.infrastructure.security.auth_service import AuthService
from app.interfaces.dependencies.order_dependency import get_order_service
from app.interfaces.schemas.order_schemas import OrderCreate, OrderResponse, OrderUpdate


router = APIRouter(prefix='/orders', tags=['Orders'])

@router.get('/', response_model=List[OrderResponse])
async def get_orders(
    current_user = Depends(AuthService.get_current_user),
    service: OrderService = Depends(get_order_service)
):
    
    return await service.get_all()

@router.get('/{id}', response_model=OrderResponse)
async def get_order_id(
    id: int,
    current_user = Depends(AuthService.get_current_user),
    service: OrderService = Depends(get_order_service)
):
    
    return await service.get_order_id(id)

@router.post('/', response_model=OrderResponse)
async def create(
    order: OrderCreate,
    current_user = Depends(AuthService.get_current_user),
    service: OrderService = Depends(get_order_service)
):
    
    return await service.create(order)

@router.put('/{id}')
async def update_status(
    id: int,
    order: OrderUpdate,
    current_user = Depends(AuthService.get_current_user),
    service: OrderService = Depends(get_order_service)
): 
    return await service.update_order_status(
        order_id=id,
        user_id=current_user.id,
        order=order
    )

@router.delete('/{id}')
async def delete_order(
    id: int,
    current_user = Depends(AuthService.get_current_user),
    service: OrderService = Depends(get_order_service)
):
    return await service.deleted(id)