"""
903_replace_derived_variable_with_query.py
范例 如果我要对生产计划（production plan）做调整（adjustment），
不光要把调整的信息保存下来，还要根据调整信息修改一个累计值——后者完全可以即时计算，
而不必每次更新。

范例2 不止一个数据来源
"""


class Data(object):
    def __init__(self, amount) -> None:
        self._amount = amount

    @property
    def amount(self):
        return self._amount


class ProductionPlan:
    def __init__(self):
        self._production = 0
        self._adjustments = []

    @property
    def production(self):
        return self._production

    def apply_adjustment(self, adjustment):
        self._adjustments.append(adjustment)
        self._production += adjustment.amount


class NewProductionPlan:
    def __init__(self):
        self._adjustments = []

    @property
    def production(self):
        return sum(i.amount for i in self._adjustments)

    def apply_adjustment(self, adjustment):
        self._adjustments.append(adjustment)


if __name__ == "__main__":

    plan = ProductionPlan()
    plan.apply_adjustment(Data(3))
    plan.apply_adjustment(Data(5))

    new_plan = NewProductionPlan()
    new_plan.apply_adjustment(Data(3))
    new_plan.apply_adjustment(Data(5))
    print("origin", plan.production, ", after", new_plan.production)
    assert plan.production == new_plan.production
