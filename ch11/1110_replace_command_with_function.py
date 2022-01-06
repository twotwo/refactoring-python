"""
1110_replace_command_with_function.py
"""


def charge(customer, usage, provider):
    base_charge = customer.base_rate * usage
    return base_charge * provider.connection_charge


if __name__ == "__main__":
    customer = "..."
    usage = 1
    provider = "..."
    month_charge = charge(customer, usage, provider)
