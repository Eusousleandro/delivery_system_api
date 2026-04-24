from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict

class OrderBase(BaseModel):
    product_id: int
    quantity: int
    price: float
    status: str

class OrderCreate(OrderBase):
    user_id: int
    address: str
    delivery_fee: float 
    payment_method: str
    payment_status: str 
    items: List[OrderBase]

class OrderUpdate(OrderBase):
    status: str

class OrderItemResponse(OrderBase):
    total: float

class OrderResponse(BaseModel):
    id: int
    user_id: int
    status: str
    address: str
    delivery_fee: float
    total_price: float
    payment_method: str
    payment_status: str
    items: List[OrderItemResponse]
    created_at: datetime

model_config = ConfigDict(from_attributes=True)