from datetime import datetime
from typing import List
from decimal import Decimal
from pydantic import BaseModel, ConfigDict

from app.interfaces.schemas.order_item_schemas import OrderItemCreate, OrderItemResponse

class OrderCreate(BaseModel):
    user_id: int
    address: str
    delivery_fee: Decimal
    payment_method: str
    payment_status: str
    items: List[OrderItemCreate]

class OrderUpdate(BaseModel):
    status: str

class OrderResponse(BaseModel):
    id: int
    user_id: int
    status: str
    address: str
    delivery_fee: Decimal
    payment_method: str
    payment_status: str
    total_price: Decimal
    items: List[OrderItemResponse]
    created_at: datetime
    updated_at: datetime

model_config = ConfigDict(from_attributes=True)