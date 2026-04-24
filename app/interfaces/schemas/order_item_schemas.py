from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: Decimal

class OrderItemResponse(BaseModel):
    product_id: int
    quantity: int
    price: Decimal

model_config = ConfigDict(from_attributes=True)