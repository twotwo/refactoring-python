from dataclasses import dataclass


@dataclass
class PersonBefore:
    first_name: str
    last_name: str


class OwnerBefore:
    def __init__(self) -> None:
        self.default_owner = PersonBefore(first_name="Martin", last_name="Fowler")


class OwnerAfter:
    def __init__(self) -> None:
        self._default_owner_data = PersonBefore(first_name="Martin", last_name="Fowler")

    @property
    def default_owner(self) -> PersonBefore:
        return self._default_owner_data

    def set_default_owner(self, arg: PersonBefore):
        self._default_owner_data = arg


class PersonAfter:
    def __init__(self, first_name, last_name) -> None:
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name


if __name__ == "__main__":
    owner = OwnerAfter()
    print(owner.default_owner)

    person = PersonAfter(first_name="Martin", last_name="Fowler")
    person.__first_name = ""  # can't modify value
    assert person.first_name == "Martin"
