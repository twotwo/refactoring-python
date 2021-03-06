"""
1102_parameterize_function
"""


def base_charge(usage):
    if usage < 0:
        return usd(0)
    amount = bottom_band(usage) * 0.03 + middle_band(usage) * 0.05 + top_band(usage) * 0.07
    return usd(amount)


def usd(amount):
    return amount * 7


def bottom_band(usage):
    return min(usage, 100)


def middle_band(usage):
    return min(usage, 200) - 100 if usage > 100 else 0


def top_band(usage):
    return usage - 200 if usage > 200 else 0
