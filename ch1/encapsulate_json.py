import json
import locale
import math
from os import name
from typing import Dict, List


class Play(object):
    def __init__(self, name: str, play_type: str) -> None:
        self._name = name
        self._type = play_type

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type


class Plays(object):
    def __init__(self, data: Dict[str, Dict]) -> None:
        self._data = {id: Play(name=play["name"], play_type=play["type"]) for id, play in data.items()}

    @staticmethod
    def load_plays(json_file: str):
        with open(json_file) as f:
            data = json.load(f)
        return Plays(data)

    def get_play(self, id: str):
        return self._data[id]


class Performance(object):
    def __init__(self, play_id: str, audience: int) -> None:
        self.play_id = play_id
        self.audience = audience


class Invoice(object):
    def __init__(self, customer: str, perfs: List[Performance]) -> None:
        self._customer = customer
        self._perfs = perfs

    @property
    def customer(self):
        return self._customer

    @property
    def performances(self):
        return self._perfs

    @staticmethod
    def load_invoices(json_file: str) -> List:
        with open(json_file) as f:
            result: List[Performance] = []
            for data in json.load(f):
                customer = data["customer"]
                perfs = [Performance(perf["playID"], perf["audience"]) for perf in data["performances"]]
                result.append(Invoice(customer, perfs))
            return result


def statement(invoice: Invoice, plays: Plays):
    locale.setlocale(locale.LC_ALL, "en_US.utf-8")

    def total_amount():
        result = 0
        for perf in invoice.performances:
            result += amount_for(perf)
        return result

    def total_volume_credits():
        result = 0
        for perf in invoice.performances:
            result += volume_credits_for(perf)
        return result

    def locale_currency(this_amount):
        return locale.currency(this_amount / 100, True)

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

    result = f"Statement for {invoice.customer}\n"
    for perf in invoice.performances:
        result += f"{play_for(perf).name}: {locale_currency(amount_for(perf))} ({perf.audience} seats)\n"

    result += f"Amount owed is {locale_currency(total_amount())}\n"
    result += f"You earned {total_volume_credits()} credits\n"
    return result


if __name__ == "__main__":
    invoices = Invoice.load_invoices("./data/invoices.json")
    plays = Plays.load_plays("./data/plays.json")
    for invoice in invoices:
        result = statement(invoice, plays)
        print(result)
