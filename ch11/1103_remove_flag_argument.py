"""
1103_remove_flag_argument.py
"""


def delivery_date(order, rush: bool):
    if rush:
        return rush_delivery_date(order)
    else:
        return regular_delivery_date(order)


def rush_delivery_date(order):
    if order.delivery_state in ["MA", "CT"]:
        deliveryTime = 1
    elif order.delivery_state in ["NY", "NH"]:
        deliveryTime = 2
    else:
        deliveryTime = 3
    return order.placed_on.plus_days(1 + deliveryTime)


def regular_delivery_date(order):
    if order.delivery_state in ["MA", "CT", "NY"]:
        deliveryTime = 2
    elif order.delivery_state in ["ME", "NH"]:
        deliveryTime = 3
    else:
        deliveryTime = 4
    return order.placed_on.plus_days(2 + deliveryTime)
