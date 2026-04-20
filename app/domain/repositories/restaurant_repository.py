from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.restaurant import Restaurant

class IRestaurantRespository(ABC):

    @abstractmethod
    def get_all(self) -> List[Restaurant]:
        pass

    @abstractmethod
    def get_restaurant_id(self, restaurant: Restaurant) -> List[Restaurant]:
        pass

    @abstractmethod
    def create(self, restaurant: Restaurant) -> Restaurant:
        pass

    @abstractmethod
    def update(self, restaurant: Restaurant) -> Restaurant:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass