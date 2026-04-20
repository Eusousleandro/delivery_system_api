from abc import ABC, abstractmethod

class IUserRepository(ABC):

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def get_user_id(self):
        pass

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def update_user(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass