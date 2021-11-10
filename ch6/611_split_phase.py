from dataclasses import dataclass


def order_price_before():
    # product-id price
    row_order = "refactoring-001 1"
    price_list = {"001": 60}
    order = row_order.split()
    product_price = price_list[order[0].split("-")[1]]
    order_price = int(order[1]) * product_price
    print("order_price", order_price)


@dataclass
class Order:
    name: str
    id: str
    quantity: int


def order_price_after():
    def paser_order(raw):
        data = raw.split()
        return Order(name=data[0].split("-")[0], id=data[0].split("-")[1], quantity=int(data[1]))

    def calculate_price(order: Order, price_list):
        return order.quantity * price_list[order.id]

    row_order = "refactoring-001 1"
    price_list = {"001": 60}
    order = paser_order(row_order)
    order_price = calculate_price(order, price_list)
    print("order_price_after", order_price)


@dataclass
class Product:
    base_price: int
    discount_threshold: int
    discount_rate: float


@dataclass
class ShippingMethod:
    discount_threshold: int
    discounted_fee: int
    fee_per_case: int


def price_order_before(product: Product, quantity: int, shipping_method: ShippingMethod):
    # Calc product price: base price - discount
    base_price = product.base_price * quantity
    discount = max(quantity - product.discount_threshold, 0) * product.base_price * product.discount_rate
    # Calc shipping cost
    shippingPerCase = (
        shipping_method.discounted_fee
        if base_price > shipping_method.discount_threshold
        else shipping_method.fee_per_case
    )
    shippingCost = quantity * shippingPerCase
    price = base_price - discount + shippingCost
    return price


def price_order_after(product: Product, quantity: int, shipping_method: ShippingMethod):
    # Calc product price: base price - discount
    price_data = calculate_pricing_data(product, quantity)
    # Calc shipping cost
    return apply_shipping(price_data, shipping_method)


def calculate_pricing_data(product: Product, quantity: int):
    # Calc product price: base price - discount
    base_price = product.base_price * quantity
    discount = max(quantity - product.discount_threshold, 0) * product.base_price * product.discount_rate
    return {"basePrice": base_price, "discount": discount, "quantity": quantity}


def apply_shipping(price_data, shipping_method: ShippingMethod):
    shippingPerCase = (
        shipping_method.discounted_fee
        if price_data["basePrice"] > shipping_method.discount_threshold
        else shipping_method.fee_per_case
    )
    shippingCost = price_data["quantity"] * shippingPerCase
    return price_data["basePrice"] - price_data["discount"] + shippingCost


if __name__ == "__main__":
    order_price_before()
    order_price_after()

    product = Product(base_price=10, discount_threshold=2, discount_rate=0.3)
    shipping_method = ShippingMethod(discount_threshold=88, discounted_fee=5, fee_per_case=1)
    print(price_order_before(product, 3, shipping_method))
    print(price_order_after(product, 3, shipping_method))
