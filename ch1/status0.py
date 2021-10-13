import locale
import math

from __init__ import Invoice, Plays


def statement(invoice: Invoice, plays: Plays):
    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice.customer}\n"

    locale.setlocale(locale.LC_ALL, "en_US.utf-8")

    for perf in invoice.performances:
        play = plays.get_play(perf.play_id)
        this_amount = 0

        if play.type == "tragedy":
            this_amount = 40000
            if perf.audience > 30:
                this_amount += 1000 * (perf.audience - 30)

        elif play.type == "comedy":
            this_amount = 30000
            if perf.audience > 20:
                this_amount += 10000 + 500 * (perf.audience - 20)
            this_amount += 300 * perf.audience
        else:
            raise Exception(f"unkownn type: {play.type}")

        volume_credits += max(perf.audience - 30, 0)

        if "comedy" == play.type:
            volume_credits += math.floor(perf.audience / 5)
        result += f"  {play.name}: {locale.currency(this_amount / 100, True)} ({perf.audience} seats)\n"
        total_amount += this_amount

    result += f"Amount owed is {locale.currency(total_amount / 100, True)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result


if __name__ == "__main__":
    invoices = Invoice.load_invoices("./data/invoices.json")
    plays = Plays.load_plays("./data/plays.json")
    for invoice in invoices:
        result = statement(invoice, plays)
        print(result)
