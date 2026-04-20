from sqlalchemy.orm import Session

from app.domain.repositories.restaurant_repository import IRestaurantRepository
from app.infrastructure.database.models.restaurant import Restaurant
from app.interfaces.schemas.restaurant_schemas import RestaurantUpdate


class RestaurantRepository(IRestaurantRepository):
    def __init__(self, db: Session):
        self.db = db
    
    async def get_all(self):
        return self.db.query(Restaurant).all()
    
    async def get_restaurant_id(self, id: int):
        return self.db.query(Restaurant).filter(Restaurant.id == id)
    
    async def create(self, restaurant: Restaurant):
        new_restaurant = Restaurant(**restaurant.dict())
        self.db.add(new_restaurant)
        self.db.commit()
        self.db.refresh(new_restaurant)
        return new_restaurant
    
    async def update(self, id: int, restaurant: RestaurantUpdate):
        restaurant_update = self.db.query(Restaurant).filter(Restaurant.id == id).first()
        restaurant_data = restaurant.model_dump(exclude_unset=True)

        for key, value in restaurant_data.items():
            setattr(restaurant_update, key, value)

        self.db.commit()
        self.db.refresh(restaurant_update)
        return restaurant_update
    
    async def delete(self, id: int):
        restaurant_delete = self.db.query(Restaurant).filter(Restaurant.id == id).first()
        self.db.delete(restaurant_delete)
        self.db.commit()
        return restaurant_delete