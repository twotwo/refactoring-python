# before


class AccountType:
    def __init__(self, name) -> None:
        self._name = name


class Account:
    def __init__(self, number, type_instance: AccountType, interest_rate) -> None:
        self._number = number
        self._type = type_instance
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate


# after
class NewAccountType:
    def __init__(self, name, interest_rate) -> None:
        self._name = name
        self.interest_rate = interest_rate


class NewAccount:
    def __init__(self, number, type_instance: NewAccountType) -> None:
        self._number = number
        self._type = type_instance

    @property
    def interest_rate(self):
        return self._type.interest_rate


if __name__ == "__main__":
    account_type = AccountType("normal")
    account = Account(10, account_type, 0.98)

    new_account_type = NewAccountType("normal", 0.98)
    new_account = NewAccount(10, new_account_type)

    assert account.interest_rate == new_account.interest_rate
