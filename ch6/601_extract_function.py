from dataclasses import dataclass


@dataclass
class Invoice:
    customer: str


def calculate_outstanding():
    return 100


def print_owing_before(invoice):
    # print_banner()
    outstanding = calculate_outstanding()

    # print details
    print(f"name: {invoice.customer}")
    print(f"amount: {outstanding}")


def print_owing_after(invoice):
    # print_banner()
    outstanding = calculate_outstanding()

    def print_details(outstanding):
        print(f"name: {invoice.customer}")
        print(f"amount: {outstanding}")

    print_details(outstanding)


if __name__ == "__main__":
    invoice = Invoice(customer="Mr. Li")
    print_owing_after(invoice)
