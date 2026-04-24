from pydantic import BaseModel, ConfigDict


class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float
    status: str

model_config = ConfigDict(from_attributes=True)