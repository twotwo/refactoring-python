"""
1208_extract_superclass.py
"""


from typing import List


class Employee:
    def __init__(self, name, id, monthly_cost):
        self._id = id
        self._name = name
        self._monthly_cost = monthly_cost

    @property
    def monthly_cost(self):
        return self._monthly_cost

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def annual_cost(self):
        return self._monthly_cost * 12


class Department:
    def __init__(self, name, staff: List[Employee]):
        self._name = name
        self._staff = staff

    @property
    def staff(self):
        return self._staff[:]

    @property
    def name(self):
        return self._name

    @property
    def total_monthly_cost(self):
        return sum([s._monthly_cost for s in self._staff])

    @property
    def head_count(self):
        return len(self._staff)

    @property
    def total_annual_cost(self):
        return self.total_monthly_cost * 12


if __name__ == "__main__":
    employee = Employee(id=1, name="jack", monthly_cost=12)
    print("Employee", employee.name, employee.annual_cost)
    department = Department(name="IT", staff=[employee, Employee(id=2, name="rose", monthly_cost=8)])
    print("Department", department.name, department.total_annual_cost)
