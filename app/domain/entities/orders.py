class OrderItem:
    def __init__(self, product_id: int, quantity: int, price: float):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def total(self) -> float:
        return self.quantity * self.price
        