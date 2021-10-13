import locale

from __init__ import Invoice, Plays
from _statement import StatementData, create_statement_data


def statement(invoice: Invoice, plays: Plays):
    return render_plain_text(create_statement_data(invoice, plays))


def render_plain_text(data: StatementData):
    result = f"Statement for {data.customer}\n"
    for perf in data.performances:
        result += f"  {perf.play.name}: {usd(perf.amount)} ( {perf.audience} seats)\n"

    result += f"Amount owed is {usd(data.total_amount)}\n"
    result += f"You earned {data.total_volume_credits} credits\n"
    return result


def usd(a_number):
    locale.setlocale(locale.LC_ALL, "en_US.utf-8")
    return locale.currency(a_number / 100)


if __name__ == "__main__":
    invoices = Invoice.load_invoices("./data/invoices.json")
    plays = Plays.load_plays("./data/plays.json")
    for invoice in invoices:
        result = statement(invoice, plays)
        print(result)
