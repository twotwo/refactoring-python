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


# 701 Transform Function


def enrich_reading(original):
    result = original.copy()
    result["baseCharge"] = base_rate(original["month"], original["year"]) * original["quantity"]
    result["taxableCharge"] = max(0, result["baseCharge"] - tax_threshold(original["year"]))
    return result


def block3_after():
    """third block: calculate basic charge"""
    raw_reading = acquire_reading()
    reading = enrich_reading(raw_reading)

    basic_charge_amount = reading["baseCharge"]
    print("basic_charge_amount", basic_charge_amount)


def block1_after():
    """first block: calculate basic charge"""
    raw_reading = acquire_reading()
    reading = enrich_reading(raw_reading)

    basic_charge = reading["baseCharge"]
    print("basic_charge", basic_charge)


def block2_after():
    """second block: calculate tax charge"""
    raw_reading = acquire_reading()
    reading = enrich_reading(raw_reading)
    taxable_charge = reading["taxableCharge"]
    print("taxable_charge", taxable_charge)


if __name__ == "__main__":
    block3_after()
    block1_after()
    block2_after()
