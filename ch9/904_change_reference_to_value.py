"""
904_change_reference_to_value.py

设想一个代表“人”的Person类，其中包含一个代表“电话号码”的Telephone Number对象。
"""
from __future__ import annotations

from dataclasses import dataclass


class Person:
    def __init__(self, telephone_number: TelephoneNumber, name):
        self._telephone_number = telephone_number
        self._name = name

    def __repr__(self) -> str:
        return f"Person(telephone_number={self._telephone_number}, name={self._name})"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, arg):
        self._name = arg

    @property
    def telephone_number(self):
        return self._telephone_number

    @property
    def office_area_code(self):
        return self._telephone_number.area_code

    @property
    def office_number(self):
        return self._telephone_number.number

    @office_number.setter
    def office_number(self, arg):
        self._telephone_number.office_number = arg


@dataclass
class TelephoneNumber:
    area_code: str
    number: str

    def __repr__(self):
        return f"{self.area_code}-{self.number}"


# STEP 1: 检查重构目标是否为不可变对象，或者是否可修改为不可变对象。
# STEP 2: 提供一个基于值的相等性判断函数，在其中使用值对象的字段。


@dataclass
class NewPerson:
    telephone_number: TelephoneNumber
    name: str

    @property
    def office_area_code(self):
        return self.telephone_number.area_code

    # STEP 3: 用 11.7-移除设值函数（331）逐一去掉所有设值函数。
    @office_area_code.setter
    def office_area_code(self, arg):
        self.telephone_number = TelephoneNumber(arg, self.office_number)

    @property
    def office_number(self):
        return self.telephone_number.number


if __name__ == "__main__":
    person = Person(TelephoneNumber("010", "66664321"), "Tom")
    new_person = NewPerson(TelephoneNumber("010", "66664321"), "Tom")
    print(person, new_person)
    assert str(person.telephone_number) == str(new_person.telephone_number)
    assert person.office_area_code == new_person.office_area_code
    assert person.office_number == new_person.office_number
