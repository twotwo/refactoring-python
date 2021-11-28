from dataclasses import dataclass
from typing import List


@dataclass
class Person:
    name: str
    age: int
    salary: int


def calc_age_and_salary(info: List[Person]):
    youngest = 100
    total_salary = 0

    for p in info:
        if p.age < youngest:
            youngest = p.age
        total_salary += p.salary

    return youngest, total_salary


def calc_age_and_salary_stage1(info: List[Person]):
    youngest = 100
    total_salary = 0

    for p in info:
        if p.age < youngest:
            youngest = p.age

    for p in info:
        total_salary += p.salary
    return youngest, total_salary


def calc_age_and_salary_stage2(info: List[Person]):
    def youngest_age():
        youngest = 100
        for p in info:
            if p.age < youngest:
                youngest = p.age
        return youngest

    def total_salary():
        total_salary = 0
        for p in info:
            total_salary += p.salary
        return total_salary

    return youngest_age(), total_salary()


def calc_age_and_salary_stage3(info: List[Person]):
    def youngest_age():
        return min([p.age for p in info])

    def total_salary():
        return sum([p.salary for p in info])

    return youngest_age(), total_salary()


if __name__ == "__main__":
    info = [
        Person("adam", 28, 1200),
        Person("bob", 31, 1500),
        Person("coco", 25, 1000),
    ]
    print("=== origin ===\n", calc_age_and_salary(info))
    print("=== stage1 ===\n", calc_age_and_salary_stage1(info))
    print("=== stage2(6.1 Extract Function) ===\n", calc_age_and_salary_stage2(info))
    print("=== stage3(8.8 Replace Loop with Pipeline) ===\n", calc_age_and_salary_stage3(info))
