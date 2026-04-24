# from fastapi import Depends
# from sqlalchemy.orm import Session

# from app.config.dependency_db import Dependencies


# def get_order_service(db: Session = Depends(Dependencies.get_db)) -> RestaurantService:
#     repository = RestaurantRepository(db)
#     return RestaurantService(repository)