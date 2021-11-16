from dataclasses import dataclass
from typing import List


# before
organization = {"name": "Acme Gooseberries", "country": "GB"}

# after
@dataclass
class Organization:
    name: str
    country: str


@dataclass
class Person:
    courses: List[str]

    def add_course(self, course: str):
        self.courses.append(course)

    def remove_course(self, course: str):
        self.courses.remove(course)


if __name__ == "__main__":
    org = Organization(name="Acme Gooseberries", country="GB")
    print("organization", organization)
    print("Organization", org)

    person = Person(["mathematics"])
    person.add_course("physics")
    person.remove_course("mathematics")
    print("person", person)
