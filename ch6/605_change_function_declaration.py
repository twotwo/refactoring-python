from dataclasses import dataclass


@dataclass
class Address:
    state: str


@dataclass
class Customer:
    address: Address


def in_new_england_before(customer):
    return customer.address.state in ["MA", "CT", "ME", "VT", "NH", "RI"]


def in_new_england_603(customer):
    state_code = customer.address.state
    return state_code in ["MA", "CT", "ME", "VT", "NH", "RI"]


def in_new_england_601(customer):
    state_code = customer.address.state
    return xxx_new_england(state_code)


def xxx_new_england(state_code):
    return state_code in ["MA", "CT", "ME", "VT", "NH", "RI"]


def in_new_england_after(state_code):
    return state_code in ["MA", "CT", "ME", "VT", "NH", "RI"]


if __name__ == "__main__":
    customer = Customer(address=Address(state="CA"))
    print(in_new_england_before(customer))
    print(in_new_england_after(state_code="CA"))
