"""
1203_pull_up_constructor_body.py

范例1 雇员的例子(在 12.1 和 12.8 也有引用)。

范例2 Employee 和 Manager，在 12.6 也有引用

"""


class Party:
    """契约或争论的）当事人，一方"""

    # Party的两个子类间存在公共代码，也即是对名字（name）的赋值
    def __init__(self, name) -> None:
        self._name = name


class Employee1(Party):
    def __init__(self, name, id, monthly_cost):
        super().__init__(name)
        self._name = id
        self._monthly_cost = monthly_cost


class Department(Party):
    def __init__(self, name, staff):
        super().__init__(name)
        self._staff = staff


# 范例2 Employee 和 Manager，无法简单地提升 `isPrivileged` 函数至超类


class Employee:
    def __init__(self, name):
        self._name = name

    def finish_construction(self):
        pass

    def is_privileged(self) -> bool:
        return False

    def assign_car(self):
        pass


class Manager(Employee):
    def __init__(self, name, grade) -> None:
        super().__init__(name)
        self._grade = grade
        self.finish_construction

    def finish_construction(self):
        self.is_privileged and self.assign_car()

    @property
    def is_privileged(self):
        return self._grade > 4
