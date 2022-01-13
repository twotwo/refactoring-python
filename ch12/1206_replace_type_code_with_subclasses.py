"""
1206_replace_type_code_with_subclasses.py

范例 员工管理系统的例子
"""


class Employee:
    def __init__(self, name, type_code) -> None:
        self.validate_type(type_code)
        self._name = name
        self._type_code = type_code

    def validate_type(arg):
        if arg not in ["engineer", "salesman", "manager"]:
            raise RuntimeError(f"Employee cannot be of type {arg}")

    def __repr__(self) -> str:
        return f"{self._name} {self._type_code}"

    @property
    def type_code(self):  # 用 6.6-封装变量（132）将类型码自封装起来
        return self._type_code


class Engineer(Employee):
    def __init__(self, name, type_code) -> None:
        super().__init__(name, "engineer")

    @property
    def type_code(self):
        return "engineer"


class Salesman(Employee):
    def __init__(self, name, type_code) -> None:
        super().__init__(name, "salesman")

    @property
    def type_code(self):
        return "engineer"


class Manager(Employee):
    def __init__(self, name, type_code) -> None:
        super().__init__(name, "engineer")

    @property
    def type_code(self):
        return "manager"


def createEmployee(name, type_code):
    return Employee(name, type_code)


def createEmployee(name, type_code):
    if type_code == "engineer":
        return Engineer(name)
    if type_code == "salesman":
        return Salesman(name)
    if type_code == "manager":
        return Manager(name)
