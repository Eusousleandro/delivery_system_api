from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.user import User

class IUserRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def get_user_id(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    def create(self, user: User) -> None:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass