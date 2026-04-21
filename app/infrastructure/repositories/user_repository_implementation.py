from sqlalchemy.orm import Session

from app.domain.repositories.user_repository import IUserRepository
from app.infrastructure.database.models.user import User
from app.interfaces.schemas.user_schema import UserUpdate


class UserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db
        
    async def get_all(self):
        return self.db.query(User).all()
    
    async def get_user_id(self, id: int):
        return self.db.query(User).filter(User.id == id).first()
    
    async def get_user_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    async def create(self, user: User):
        new_user = User(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    async def update(self, id: int, user: UserUpdate):
        user_update = self.db.query(User).filter(User.id == id).first()
        user_data = user.model_dump(exclude_unset=True)

        for key, value in user_data.items():
            setattr(user_update, key, value)

        self.db.commit()
        self.db.refresh(user_update)
        return user_update
    
    async def delete(self, id: int):
        user_delete = self.db.query(User).filter(User.id == id).first()
        self.db.delete(user_delete)
        self.db.commit()
        return user_delete