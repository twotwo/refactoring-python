"""
1001_decompose_conditional.py

要计算购买某样商品的总价（总价=数量×单价），而这个商品在冬季和夏季的单价是不同的

"""
from dataclasses import dataclass


@dataclass
class Plan:
    quantity: int
    month: int
    summer_rate: float
    regular_rate: float
    regular_service_charge: float

    def summer(self):
        return self.month > 6 and self.month < 10

    def summer_charge(self):
        return self.quantity * self.summer_rate

    def regular_charge(self):
        return self.quantity * self.regular_rate + self.regular_service_charge


def charge_before(plan: Plan):
    if plan.month > 6 and plan.month < 10:
        return plan.quantity * plan.summer_rate
    else:
        return plan.quantity * plan.regular_rate + plan.regular_service_charge


def new_charge(plan: Plan):
    return plan.summer_charge() if plan.summer() else plan.regular_charge()


if __name__ == "__main__":
    plan = Plan(quantity=10, month=7, summer_rate=1, regular_rate=0.8, regular_service_charge=5)
    print("origin", charge_before(plan), "new", new_charge(plan))
    assert charge_before(plan) == new_charge(plan)
