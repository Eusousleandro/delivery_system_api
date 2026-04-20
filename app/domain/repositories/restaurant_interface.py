from abc import ABC, abstractmethod

class IRestaurant(ABC):

    @abstractmethod
    def get_restaurants(self):
        pass

    @abstractmethod
    def get_restaurant_id(self):
        pass

    @abstractmethod
    def create_restaurant(self):
        pass
    
    @abstractmethod
    def update_restaurant(self):
        pass

    @abstractmethod
    def delete_restaurant(self):
        pass