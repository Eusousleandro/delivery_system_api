from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.infrastructure.database.connection import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("Order", back_populates="items")