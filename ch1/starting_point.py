import json
import locale
import math
from typing import Dict, List


def statement(invoice: Dict, plays: Dict):
    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice['customer']}\n"

    locale.setlocale(locale.LC_ALL, "en_US.utf-8")

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        this_amount = 0

        if play["type"] == "tragedy":
            this_amount = 40000
            if perf["audience"] > 30:
                this_amount += 1000 * (perf["audience"] - 30)

        elif play["type"] == "comedy":
            this_amount = 30000
            if perf["audience"] > 20:
                this_amount += 10000 + 500 * (perf["audience"] - 20)
            this_amount += 300 * perf["audience"]
        else:
            raise Exception(f"unkownn type: {play['type']}")

        volume_credits += max(perf["audience"] - 30, 0)

        if "comedy" == play["type"]:
            volume_credits += math.floor(perf["audience"] / 5)
        result += f"  {play['name']}: {locale.currency(this_amount / 100, True)} ({perf['audience']} seats)\n"
        total_amount += this_amount

    result += f"Amount owed is {locale.currency(total_amount / 100, True)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result


if __name__ == "__main__":
    with open("./data/invoices.json") as f:
        invoices: List[Dict] = json.load(f)
    with open("./data/plays.json") as f:
        plays = json.load(f)
    for invoice in invoices:
        result = statement(invoice, plays)
        print(result)
