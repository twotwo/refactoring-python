from typing import List


class Course:
    def __init__(self, name, is_advanced):
        self._name = name
        self._is_advanced = is_advanced

    @property
    def name(self):
        return self._name

    @property
    def is_advanced(self):
        return self._is_advanced

    def __repr__(self) -> str:
        return f"{self.name} advanced?{self.is_advanced}"


class Person:
    def __init__(self, name):
        self._name = name
        self._courses: List[Course] = []

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, courses: List):
        print("set attribute courses. don't use this anotation!")
        self._courses = courses

    def __repr__(self) -> str:
        return f"Person(name={self.name}, courses={self.courses})"


class NewPerson:
    def __init__(self, name: str, cources: List[Course]):
        self._name = name
        self._courses: List[Course] = cources

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return self._courses.copy()

    def add_course(self, course):
        print(f"add new course {course} in person")
        self._courses.append(course)

    def remove_course(self, course):
        assert course in self._courses
        self._courses.remove(course)

    def __repr__(self) -> str:
        return f"NewPerson(name={self.name}, courses={self.courses})"


if __name__ == "__main__":
    person = Person(name="Tom")
    basic_courses = ["MUSIC", "MATH", "SPORTS"]
    person.courses = [Course(name, True) for name in basic_courses]  # set attribute
    print("init person", person)
    for name in basic_courses:
        person.courses.append(Course(name, False))
    print("add new courses", person)
    num_advanced_courses = len([i for i in person.courses if not i.is_advanced])

    new_person = NewPerson(name="Tom", cources=[Course(name, True) for name in basic_courses])
    try:
        new_person.courses = []
    except AttributeError as ex:
        print("can't set attribute on new_person.courses:", ex)
    print("init person", new_person)
    for name in new_person.courses:
        new_person.add_course(Course(name, False))
    print("add new courses", new_person)
    new_num_advanced_courses = sum(map(lambda x: not x.is_advanced, new_person.courses))
    assert new_num_advanced_courses == num_advanced_courses
