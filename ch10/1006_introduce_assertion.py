"""
1006_introduce_assertion.py
"""


class Customer:
    def apply_discount(self, number):
        return number - self.discount_rate * number if self.discount_rate else number


class Customer1:
    def apply_discount(self, number):
        if not self.discount_rate:
            return number
        assert self.discount_rate >= 0
        return number - self.discount_rate * number


class Customer2:
    def __init__(self, discount_rate) -> None:
        assert discount_rate is None or discount_rate >= 0
        self.discount_rate = discount_rate

    def apply_discount(self, number):
        if not self.discount_rate:
            return number
        return number - self.discount_rate * number
