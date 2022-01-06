"""
1110_replace_command_with_function.py
"""


class ChargeCalculator:
    def __init__(self, customer, usage, provider) -> None:
        self._customer = customer
        self._usage = usage
        self._provider = provider

    @property
    def base_charge(self):
        return self._customer.base_rate * self._usage

    @property
    def charge(self):
        return self.base_charge * self._provider.connection_charge


if __name__ == "__main__":
    customer = "..."
    usage = 1
    provider = "..."
    month_charge = ChargeCalculator(customer, usage, provider).charge
