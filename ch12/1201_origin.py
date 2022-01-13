"""
1201_pull_up_method.py

范例 有两个子类，它们之中各有一个函数做了相同的事情。这个例子在 12.8 也有引用。
"""


class Party:
    """契约或争论的）当事人，一方"""


class Employee(Party):
    @property
    def annual_cost(self):
        return self._monthly_cost * 12


class Department(Party):
    @property
    def total_annual_cost(self):
        return self.total_monthly_cost * 12
