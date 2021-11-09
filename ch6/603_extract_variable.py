from dataclasses import dataclass
from typing import List


@dataclass
class Order:
    quantity: int
    item_price: int


def price_before(order: Order):
    #   price is base price - quantity discount + shipping
    return (
        order.quantity * order.item_price
        - max(0, order.quantity - 500) * order.item_price * 0.05
        + min(order.quantity * order.item_price * 0.1, 100)
    )


def price_after(order: Order):
    base_price = order.quantity * order.item_price
    quantity_discount = max(0, order.quantity - 500) * order.item_price * 0.05
    shipping = min(base_price * 0.1, 100)
    return base_price - quantity_discount + shipping


class OrderBefore(object):
    def __init__(self, record) -> None:
        self._data = record

    @property
    def quantity(self):
        return self._data.quantity

    @property
    def item_price(self):
        return self._data.item_price

    @property
    def price(self):
        return (
            self.quantity * self.item_price
            - max(0, self.quantity - 500) * self.item_price * 0.05
            + min(self.quantity * self.item_price * 0.1, 100)
        )


class OrderAfter(object):
    def __init__(self, record) -> None:
        self._data = record

    @property
    def quantity(self):
        return self._data.quantity

    @property
    def item_price(self):
        return self._data.item_price

    @property
    def price(self):
        return self.base_price - self.quantity_discount + self.shipping

    @property
    def base_price(self):
        return self.quantity * self.item_price

    @property
    def quantity_discount(self):
        return max(0, self.quantity - 500) * self.item_price * 0.05

    @property
    def shipping(self):
        return min(self.base_price * 0.1, 100)


if __name__ == "__main__":
    order = OrderAfter(Order(quantity=100, item_price=10))
    print(order.price)
