"""
1105_replace_parameter_with_query.py
"""


class Order:
    @property
    def final_price(self):
        base_price = self.quantity * self.item_price
        return self.discounted_price(base_price)

    @property
    def discount_level(self):
        return 2 if self.quantity > 100 else 1

    def discounted_price(self, base_price):
        if self.discount_level == 1:
            return base_price * 0.95
        if self.discount_level == 2:
            return base_price * 0.9
