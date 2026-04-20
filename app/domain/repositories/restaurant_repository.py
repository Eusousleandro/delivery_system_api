from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.restaurant import Restaurant

class IRestaurantRespository(ABC):

    @abstractmethod
    def get_all(self, restaurant: Restaurant) -> List[Restaurant]:
        pass

    @abstractmethod
    def get_restaurant_id(self, restaurant: Restaurant):
        pass

    @abstractmethod
    def create_restaurant(self, restaurant: Restaurant):
        pass

    @abstractmethod
    def update_restaurant(self, restaurant: Restaurant):
        pass

    @abstractmethod
    def delete_restaurant(self, restaurant: Restaurant):
        pass