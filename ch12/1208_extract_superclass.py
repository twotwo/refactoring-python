"""
1208_extract_superclass.py
"""


class Party:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def annual_cost(self):
        return self._annual_cost


class Employee(Party):
    def __init__(self, name, id, monthly_cost):
        super().__init__(name)
        self._id = id
        self._monthly_cost = monthly_cost

    @property
    def monthly_cost(self):
        return self._monthly_cost

    @property
    def id(self):
        return self._id

    @property
    def annual_cost(self):
        return self._monthly_cost * 12


class Department(Party):
    def __init__(self, name, staff):
        super().__init__(name)
        self._staff = staff

    @property
    def staff(self):
        return self._staff[:]

    @property
    def monthly_cost(self):
        return sum([s._monthly_cost for s in self._staff])

    @property
    def head_count(self):
        return len(self._staff)

    @property
    def annual_cost(self):
        return self.monthly_cost * 12


if __name__ == "__main__":
    employee = Employee(id=1, name="jack", monthly_cost=12)
    print("Employee", employee.name, employee.annual_cost)
    department = Department(name="IT", staff=[employee, Employee(id=2, name="rose", monthly_cost=8)])
    print("Department", department.name, department.annual_cost)
