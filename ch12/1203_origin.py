"""
1203_pull_up_constructor_body.py

范例 雇员的例子(在 12.1 和 12.8 也有引用)。
"""


class Party:
    """契约或争论的）当事人，一方"""


class Employee1(Party):
    def __init__(self, name, id, monthly_cost):
        super().__init__()
        self._name = name
        self._name = id
        self._monthly_cost = monthly_cost


# 范例2 Employee 和 Manager，无法简单地提升 `isPrivileged` 函数至超类


class Employee:
    def __init__(self, name):
        self._name = name

    def assign_car(self):
        pass


class Manager(Employee):
    def __init__(self, name, grade) -> None:
        super().__init__(name)
        self._grade = grade
        self.is_privileged and self.assign_car()

    @property
    def is_privileged(self) -> bool:
        return self._grade > 4
