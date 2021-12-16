"""
1002_consolidate_conditional_expression.py

范例1 使用逻辑或

范例2 使用逻辑与
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Employee:
    seniority: int
    months_disabled: int
    part_time: bool
    on_vacation: bool

    def is_not_eligible_for_disablility(self):
        return self.seniority < 2 or self.months_disabled > 12 or self.part_time


def disability_amount(employee: Employee):
    if employee.seniority < 2:
        return 0
    if employee.months_disabled > 12:
        return 0
    if employee.part_time:
        return 0

    if employee.on_vacation:
        if employee.seniority > 10:
            return 1
    return 0.5


def new_disability_amount(employee: Employee):
    if employee.is_not_eligible_for_disablility():
        return 0
    if employee.on_vacation and employee.seniority > 10:
        return 1
    return 0.5


if __name__ == "__main__":
    employee = Employee(10, 0, False, True)
    print("origin", disability_amount(employee), "new", new_disability_amount(employee))
