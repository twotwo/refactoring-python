import locale
import math

from __init__ import Invoice, Plays


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
