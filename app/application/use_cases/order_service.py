from typing import List

from app.domain.exceptions.exception import AlreadyExistsException, CreatedonFailedException, DeletionFailedException, NotFoundException, UpdatedonFailedException
from app.infrastructure.repositories.order_repository_implementation import OrderRepository
from app.interfaces.mappers.order_mapper import to_orders_reponse
from app.interfaces.schemas.order_schemas import OrderCreate, OrderUpdate
from app.infrastructure.websockets.connection_manager import manager


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    async def get_all(self) -> List[dict]:
        orders = await self.repository.get_all()
        if not orders:
            raise NotFoundException()
        
        return [to_orders_reponse(o) for o in orders]
    
    async def get_order_id(self, id: int) -> dict:
        order = await self.repository.get_order_id(id)
        if not order:
            raise NotFoundException()
        
        return to_orders_reponse(order)
    
    async def create(self, order: OrderCreate) -> dict:
        order_existing = await self.repository.get_order_id(order.user_id)
        if not order_existing:
            raise NotFoundException()
        
        created_order = self.repository.create(order)
        if not created_order: 
            raise CreatedonFailedException()
        
        return created_order
    
    async def update_order_status(self, order_id, user_id: int,
            status: str, order: OrderUpdate) -> dict:
        order_existing = await self.repository.get_order_id(id)
        if order_existing:
            raise AlreadyExistsException()
        
        await manager.send_to_user(
            user_id=user_id,
            message={
                'event': 'ORDER_UPDATED',
                'order_id': order_id,
                'status': status
            }
        )
        
        order_update = await self.repository.update(order)
        if not order_update:
            raise UpdatedonFailedException()
        
        return {'message': 'Order updated', 'Order:': order_update}
    
    async def deleted(self, id: int) -> None:
        order_existing = await self.repository.get_order_id(id)
        if not order_existing:
            raise NotFoundException()
        
        order_delete = await self.repository.delete(id)
        if not order_delete:
            raise DeletionFailedException()
        
        return order_delete
