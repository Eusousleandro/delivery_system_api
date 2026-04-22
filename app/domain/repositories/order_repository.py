from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.orders import OrderItem

class IOrderRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[OrderItem]:
        pass

    @abstractmethod
    def get_order_id(self, id: int) -> Optional[OrderItem]:
        pass

    @abstractmethod
    def create(self, order: OrderItem) -> None:
        pass

    @abstractmethod
    def update(self, id: int, order: OrderItem) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass