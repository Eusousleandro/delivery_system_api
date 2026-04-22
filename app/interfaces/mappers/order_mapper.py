from app.infrastructure.database.models.order import Order
from app.interfaces.schemas.order_schemas import OrderResponse


def to_orders_reponse(order: Order) -> OrderResponse:
    return OrderResponse(

    )