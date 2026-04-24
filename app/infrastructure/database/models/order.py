from sqlalchemy import Column, DateTime, Float, Integer, Numeric, String, func
from sqlalchemy.orm import relationship

from app.infrastructure.database.connection import Base
from app.infrastructure.database.models.order_items import OrderItem


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), default=0.0)
    status = Column(String(50), nullable=False, default="PENDING")
    address = Column(String(250), nullable=False)
    delivery_fee = Column(Numeric(10, 2), default=0.0, nullable=False)
    payment_method = Column(String(250), nullable=False)
    payment_status = Column(String(250), nullable=False)
    items = relationship(OrderItem, back_populates="order")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())