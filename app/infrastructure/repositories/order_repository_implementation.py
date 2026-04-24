from sqlalchemy.orm import Session

from app.domain.repositories.order_repository import IOrderRepository
from app.infrastructure.database.models.order import Order
from app.interfaces.schemas.order_schemas import OrderCreate, OrderUpdate

class OrderRepository(IOrderRepository):
    def __init__(self, db: Session):
        self.db = db

    async def get_all(self):
        return self.db.query(Order).all()
    
    async def get_order_id(self, id: int):
        return self.db.query(Order).filter(Order.id == id).first()
    
    async def create(self, order: Order):
        new_order = Order(**order.model_dump())
        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        return new_order
    
    async def update(self, user_id: int, order: OrderUpdate):
        order_update = self.db.query(Order).filter(Order.id == user_id).first()
        order_data = order.model_dump(exclude_unset=True)

        for key, value in order_data.items():
            setattr(order_update, key, value)

        self.db.commit()
        self.db.refresh(order_update)
        return order_update
    
    async def delete(self, id:int):
        order_delete = self.db.query(Order).filter(Order.id == id).first()
        self.db.delete(order_delete)
        self.db.commit()
        return order_delete
        