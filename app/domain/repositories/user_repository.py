from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.user import User

class IUserRepository(ABC):

    @abstractmethod
    def get_all(self, user: User) -> List[User]:
        pass

    @abstractmethod
    def get_user_id(self, user: User):
        pass

    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def update_user(self, user: User):
        pass

    @abstractmethod
    def delete_user(self, user: User):
        pass