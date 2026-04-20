from sqlalchemy import Column, Integer, String

from app.infrastructure.database.connection import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    email = Column(String(100), unique=True, index=True)
    cnpj = Column(String(20), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)