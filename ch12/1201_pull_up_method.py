"""
1201_pull_up_method.py

范例 有两个子类，它们之中各有一个函数做了相同的事情。这个例子在 12.3 和 12.8 也有引用。
"""


class Party:
    """契约或争论的）当事人，一方"""

    @property
    def annual_cost(self):
        return self.monthly_cost * 12

    @property
    def monthly_cost(self):
        raise RuntimeError("SubclassResponsibilityError")


class Employee(Party):
    @property
    def monthly_cost(self):
        return self._monthly_cost


class Department(Party):
    """total_annual_cost() 改名为 annual_cost()"""

    @property
    def monthly_cost(self):
        return self._monthly_cost
