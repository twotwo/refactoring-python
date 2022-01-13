"""
1207_remove_subclass.py

"""
from __future__ import annotations
from collections import namedtuple


# before
class Person:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def gender_code(self):
        return "X"


class Male(Person):
    @property
    def gender_code(self):
        return "M"


class Female(Person):
    @property
    def gender_code(self):
        return "F"


# after
class Person:
    def __init__(self, name, gender_code: str = None) -> None:
        self._name = name
        self._gender_code = gender_code or "X"

    @property
    def gender_code(self):
        return self._gender_code


Record = namedtuple("Record", ["name", "gender"])


def create_person(record: Record):
    if record.gender == "M":
        return Person(record.name, record.gender)

    if record.gender == "F":
        return Person(record.name, record.gender)
    return Person(record.name)
