from app.infrastructure.database.models.restaurant import Restaurant
from app.interfaces.schemas.restaurant_schemas import RestaurantResponse


def to_restaurant_response(restaurant: Restaurant) -> RestaurantResponse:
    return RestaurantResponse(
        id=restaurant.id,
        name=restaurant.name,
        email=restaurant.email,
        cnpj=restaurant.cnpj
    )