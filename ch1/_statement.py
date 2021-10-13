import math
from typing import List

from __init__ import Invoice, Plays


class Performance4Display(object):
    def __init__(self, play, audience, amount, volume_credits) -> None:
        self.play = play
        self.audience = audience
        self.amount = amount
        self.volume_credits = volume_credits


class StatementData(object):
    def __init__(self, customer, performances, total_amount, credits) -> None:
        self.customer = customer
        self.performances: List[Performance4Display] = performances
        self.total_amount = total_amount
        self.total_volume_credits = credits


def create_statement_data(invoice: Invoice, plays: Plays) -> StatementData:
    def enrich_performance(perf):
        return Performance4Display(
            play=play_for(perf),
            audience=perf.audience,
            amount=amount_for(perf),
            volume_credits=volume_credits_for(perf),
        )

    def total_amount(performances):
        result = 0
        for perf in performances:
            result += amount_for(perf)
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

    def amount_for(perf):
        result = 0
        play = play_for(perf)
        if play.type == "tragedy":
            result = 40000
            if perf.audience > 30:
                result += 1000 * (perf.audience - 30)

        elif play.type == "comedy":
            result = 30000
            if perf.audience > 20:
                result += 10000 + 500 * (perf.audience - 20)
            result += 300 * perf.audience
        else:
            raise Exception(f"unkownn type: {play.type}")
        return result

    return StatementData(
        customer=invoice.customer,
        performances=list(map(enrich_performance, invoice.performances)),
        total_amount=total_amount(invoice.performances),
        credits=total_volume_credits(),
    )
