from sqlalchemy import Column, Integer, String
from app.infrastructure.database.connection import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)