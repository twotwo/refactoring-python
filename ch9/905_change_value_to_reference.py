"""
905_change_value_to_reference.py

从一个代表“订单”的 Order 类开始，其实例对象可从一个 JSON 文件创建。
用来创建订单的数据中有一个顾客（customer）ID，我们用它来进一步创建 Customer 对象。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


class Order:
    def __init__(self, data: Data):
        self._number = data.number
        self._customer = Customer(data.customer)

    @property
    def customer(self):
        return self._customer

@dataclass
class Data:
    number: int
    customer: int


@dataclass
class Customer:
    id: int


@dataclass
class Repository:
    customers: Dict[str, Customer] = field(default_factory=dict)


_repositoryData = Repository()


def find_customer(id):
    return _repositoryData.customers.get(id)


def register_customer(id):
    if not find_customer(id):
        _repositoryData.customers[id] = Customer(id)
    return find_customer(id)


class NewOrder:
    def __init__(self, data: Data):
        self._number = data.number
        self._customer = register_customer(data.customer)

    @property
    def customer(self):
        return self._customer


if __name__ == "__main__":
    order = Order(Data(111, 999))
    new_order = NewOrder(Data(111, 999))
    print("origin", order, "after", new_order)
    assert order.customer == new_order.customer
