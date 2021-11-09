_reading = {"customer": "ivan", "quantity": 10, "month": 5, "year": 2017}


def acquire_reading():
    return _reading


def base_rate(month: int, year: int):
    """query tax base rate by year and month"""
    return 1


def tax_threshold(year: int):
    """query tax threshold by year"""
    return 10


def block1_before():
    """first block: calculate basic charge"""
    reading = acquire_reading()
    basic_charge = base_rate(reading["month"], reading["year"]) * reading["quantity"]
    print("basic_charge", basic_charge)


def block2_before():
    """second block: calculate tax charge"""
    reading = acquire_reading()
    base = base_rate(reading["month"], reading["year"]) * reading["quantity"]  # calc twice
    taxable_charge = max(0, base - tax_threshold(reading["year"]))
    print("taxable_charge", taxable_charge)


def block3_before():
    """third block: calculate basic charge"""
    reading = acquire_reading()

    def calculate_base_charge():
        return base_rate(reading["month"], reading["year"]) * reading["quantity"]

    basic_charge_amount = calculate_base_charge()
    print("basic_charge_amount", basic_charge_amount)


# 701 Encapsulate Record


class Reading(object):
    def __init__(self, data) -> None:
        self.__customer = data["customer"]
        self.__quantity = data["quantity"]
        self.__month = data["month"]
        self.__year = data["year"]

    @property
    def customer(self):
        return self.__customer

    @property
    def quantity(self):
        return self.__quantity

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @property
    def base_charge(self):
        return base_rate(self.month, self.year) * self.quantity

    @property
    def taxable_charge(self):
        return max(0, self.base_charge - tax_threshold(self.year))


def block3_after():
    """third block: calculate basic charge"""
    raw_reading = acquire_reading()
    reading = Reading(raw_reading)

    basic_charge_amount = reading.base_charge
    print("basic_charge_amount", basic_charge_amount)


def block1_after():
    """first block: calculate basic charge"""
    raw_reading = acquire_reading()
    reading = Reading(raw_reading)
    basic_charge = reading.base_charge
    print("basic_charge", basic_charge)


def block2_after():
    """second block: calculate tax charge"""
    raw_reading = acquire_reading()
    reading = Reading(raw_reading)
    taxable_charge = reading.taxable_charge
    print("taxable_charge", taxable_charge)


if __name__ == "__main__":
    block3_after()
    block1_after()
    block2_after()
