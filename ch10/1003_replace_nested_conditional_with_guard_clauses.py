"""
1003_replace_nested_conditional_with_guard_clauses.py

范例 将条件反转

我们常常可以将条件表达式反转，从而实现以卫语句取代嵌套条件表达式
"""
from dataclasses import dataclass


@dataclass
class Instrument:
    capital: int
    income: int
    duration: int
    interest_rate: float
    adjustment_factor: float


def adjusted_capital(instrument):
    result = 0
    if instrument.capital > 0:
        if instrument.interest_rate > 0 and instrument.duration > 0:
            result = (instrument.income / instrument.duration) * instrument.adjustment_factor
    return result


def adjusted_capital_stage1(instrument):
    result = 0
    if instrument.capital <= 0:  # reverse 1
        return result
    if not (instrument.interest_rate > 0 and instrument.duration > 0):  # reverse 2
        return result
    result = (instrument.income / instrument.duration) * instrument.adjustment_factor
    return result


def adjusted_capital_stage2(instrument):
    result = 0
    if instrument.capital <= 0:
        return result
    if instrument.interest_rate <= 0 or instrument.duration < 0:  # elimination of not logic
        return result
    result = (instrument.income / instrument.duration) * instrument.adjustment_factor
    return result


def adjusted_capital_stage3(instrument):
    if (
        instrument.capital <= 0 or instrument.interest_rate <= 0 or instrument.duration < 0
    ):  # 10.2 Consolidate Conditional Expression
        return 0
    return (instrument.income / instrument.duration) * instrument.adjustment_factor


if __name__ == "__main__":
    instrument = Instrument(capital=100, income=10, duration=10, interest_rate=0.2, adjustment_factor=0.8)
    print("origin", adjusted_capital(instrument))
    print("stage1", adjusted_capital_stage1(instrument))
    print("stage2", adjusted_capital_stage2(instrument))
    print("stage3", adjusted_capital_stage3(instrument))
