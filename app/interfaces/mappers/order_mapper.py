from app.infrastructure.database.models.order import Order
from app.interfaces.schemas.order_schemas import OrderResponse


def to_orders_reponse(order: Order) -> OrderResponse:
    return OrderResponse(
        id=order.id,
        user_id=order.user_id,
        status=order.status,
        address=order.address,
        delivery_fee=order.delivery_fee,
        payment_method=order.payment_method,
        payment_status=order.payment_status,
        items=order.items,
        created_at=order.created_at
    )