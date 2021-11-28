from dataclasses import dataclass


@dataclass
class Order:
    special_deal: bool
    price: float

    def emit_content(self):
        print("emit_content", self.total)

    def calc(self):
        if self.special_deal:
            self.total = self.price * 0.95
            self.emit_content()
        else:
            self.total = self.price * 0.98
            self.emit_content()


@dataclass
class NewOrder:
    special_deal: bool
    price: float

    def emit_content(self):
        print("emit_content", self.total)

    def calc(self):
        if self.special_deal:
            self.total = self.price * 0.95
        else:
            self.total = self.price * 0.98
        self.emit_content()


if __name__ == "__main__":
    order = Order(True, 100)
    order.calc()

    order = NewOrder(True, 100)
    order.calc()
