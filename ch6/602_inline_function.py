from dataclasses import dataclass
from typing import List


@dataclass
class Driver:
    number_of_late_deliveries: int


def get_rating_before(driver):
    return 2 if more_than_five_late_deliveries(driver) else 1


def more_than_five_late_deliveries(driver):
    return driver.number_of_late_deliveries > 5


def get_rating_after(driver):
    return 2 if driver.number_of_late_deliveries > 5 else 1


@dataclass
class Customer:
    name: str
    location: str


def report_lines_before(customer: Customer):
    lines: List[List[str]] = []
    gather_customer_data(lines, customer)
    return lines


def gather_customer_data(out: List[List[str]], customer: Customer):
    out.append(["name", customer.name])
    out.append(["location", customer.location])


def report_lines_after(customer: Customer):
    lines: List[Customer] = []
    lines.append(["name", customer.name])
    lines.append(["location", customer.location])
    return lines


if __name__ == "__main__":
    customer = Customer(name="Mr. Li", location="BJ, China")
    print(report_lines_after(customer))
