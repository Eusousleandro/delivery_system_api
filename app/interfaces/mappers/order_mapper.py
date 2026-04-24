from app.infrastructure.database.models.order import Order
from app.interfaces.schemas.order_schemas import OrderItemResponse, OrderResponse


def to_orders_reponse(order: Order) -> OrderResponse:
    return OrderResponse(
            id=order.id,
            user_id=order.user_id,
            status=order.status,
            address=order.address,
            payment_method=order.payment_method,
            payment_status=order.payment_status,
            items=[
                OrderItemResponse(
                    product_id=i.product_id,
                    quantity=i.quantity,
                    price=i.price
                )
                for i in order.items
            ]
        )