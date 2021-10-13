import math
from dataclasses import dataclass
from functools import reduce

from __init__ import Invoice, Plays
from _statement import Performance4Display, StatementData


def create_statement_data(invoice: Invoice, plays: Plays) -> StatementData:
    def enrich_performance(perf):

        calculator = create_performance_calculator(perf, play_for(perf))
        return Performance4Display(
            play=calculator.play,
            audience=perf.audience,
            amount=calculator.amount(),
            volume_credits=calculator.volume_credits(),
        )

    def total_amount(performances):
        result = 0
        for perf in performances:
            result += perf.amount
        return result

    def total_volume_credits():
        result = 0
        for perf in invoice.performances:
            result += volume_credits_for(perf)
        return result

    def volume_credits_for(perf):
        result = 0
        result += max(perf.audience - 30, 0)
        if "comedy" == play_for(perf).type:
            result += math.floor(perf.audience / 5)
        return result

    def play_for(perf):
        return plays.get_play(perf.play_id)

    performances = list(map(enrich_performance, invoice.performances))
    return StatementData(
        customer=invoice.customer,
        performances=performances,
        total_amount=total_amount(performances),
        credits=total_volume_credits(),
    )


@dataclass
class PerformanceCalculator:
    performance: dict
    play: dict

    def amount(self) -> int:
        raise Exception("Subclass responsibility")

    def volume_credits(self) -> int:
        return max(self.performance.audience - 30, 0)


class TragedyCalculator(PerformanceCalculator):
    def amount(self) -> int:
        result = 40000
        if self.performance.audience > 30:
            result += 1000 * (self.performance.audience - 30)
        return result


class ComedyCalculator(PerformanceCalculator):
    def amount(self) -> int:
        result = 30000
        if self.performance.audience > 20:
            result += 10000 + 500 * (self.performance.audience - 20)
        result += 300 * self.performance.audience
        return result

    def volume_credits(self) -> int:
        return super().volume_credits() + math.floor(self.performance.audience / 5)


def create_performance_calculator(perf, play):
    if play.type == "tragedy":
        return TragedyCalculator(perf, play)
    elif play.type == "comedy":
        return ComedyCalculator(perf, play)
    else:
        raise Exception(f"unkownn play: {play.type}")
