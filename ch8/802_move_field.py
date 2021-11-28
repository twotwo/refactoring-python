# before
class Account:
    def __init__(self, number, typeString, interestRate) -> None:
        self._number = number
        self._type = Account.AccountType(typeString)
        self._interestRate = interestRate

    @property
    def interestRate(self):
        return self._interestRate

    class AccountType:
        def __init__(self, nameString) -> None:
            self._name = nameString


# after
class AccountType:
    def __init__(self, nameString, interestRate) -> None:
        self._name = nameString
        self._interestRate = interestRate

    @property
    def interestRate(self):
        return self._interestRate


class NewAccount:
    def __init__(self, number, account_type) -> None:
        self._number = number
        self._type = account_type
