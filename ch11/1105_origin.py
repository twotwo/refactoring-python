"""
1105_replace_parameter_with_query.py
"""


class Order:
    @property
    def final_price(self):
        base_price = self.quantity * self.item_price
        if self.quantity > 100:
            discount_level = 2
        else:
            discount_level = 1
        return self.discounted_price(base_price, discount_level)

    def discounted_price(self, base_price, discount_level):
        if discount_level == 1:
            return base_price * 0.95
        if discount_level == 2:
            return base_price * 0.9
