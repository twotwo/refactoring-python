from copy import deepcopy
from dataclasses import dataclass, field
from typing import Any, Dict


# before
organization = {"name": "Acme Gooseberries", "country": "GB"}

# after
@dataclass
class Organization:
    name: str
    country: str


# before
customer_data = {
    "1920": {"name": "martin", "id": "1920", "usages": {2016: {1: 50, 2: 55}, 2015: {1: 70, 2: 63}}},
    "38673": {"name": "neal", "id": "38673"},
}


def set_amount(customer_id, year, month, amount):
    try:
        customer_data[customer_id]["usages"][year][month] = amount
    except KeyError:
        customer_data.update({customer_id: {"usages": {year: {month: amount}}}})


def compare_usage(customer_id, later_year, month):
    later = customer_data[customer_id]["usages"][later_year][month]
    earlier = customer_data[customer_id]["usages"][later_year - 1][month]
    return {"later_amount": later, "change": later - earlier}


@dataclass
class Customer:
    name: str
    id: str
    usages: Dict[str, Any] = field(default_factory=dict)

    def __iter__(self):  # to hide blank usages
        return ((key, value) for key, value in self.__dict__.items() if value)


# after
class CustomerData:
    def __init__(self, data):
        self._user_dict = {i: Customer(**j) for i, j in data.items()}

    @property
    def raw_data(self):
        return {i: dict(j) for i, j in self._user_dict.items()}

    def usage(self, customer_id, year, month):
        return self._user_dict[customer_id].usages[year][month]

    def compare_usage(self, customer_id, later_year, month):
        later = self._user_dict[customer_id].usages[later_year][month]
        earlier = self._user_dict[customer_id].usages[later_year - 1][month]
        return {"later_amount": later, "change": later - earlier}

    def set_usage(self, customer_id, year, month, amount):
        self._user_dict[customer_id].usages[year][month] = amount


if __name__ == "__main__":
    org = Organization(name="Acme Gooseberries", country="GB")
    print("organization", organization)
    print("Organization", org)

    origin_data = deepcopy(customer_data)
    set_amount("1920", 2016, 3, 40)
    print("=== origin data:\n", origin_data, "\n=== updated:\n", customer_data)

    customer_record = CustomerData(origin_data)
    customer_record.set_usage("1920", 2016, 3, 40)
    print("=== CustomerData\n", customer_record.raw_data)
