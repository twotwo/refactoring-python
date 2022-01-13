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
