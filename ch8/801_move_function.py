from dataclasses import dataclass

# before
class Account:
    def __init__(self, days_overdrawn, premium: bool) -> None:
        self._days_overdrawn = days_overdrawn
        self.type: Account.AccountType = Account.AccountType(premium)

    def bank_charge(self) -> float:
        result = 4.5
        if self._days_overdrawn > 0:
            result += self.overdraft_charge

        return result

    @property
    def overdraft_charge(self):
        if not self.type.premium:
            return self._days_overdrawn * 1.7
        base_charge = 10
        if self._days_overdrawn <= 7:
            return base_charge
        else:
            return base_charge + (self._days_overdrawn - 7) * 0.85

    @dataclass
    class AccountType:
        premium: bool


# after
@dataclass
class AccountType:
    premium: bool

    def overdraft_charge(self, days_overdrawn):
        if not self.premium:
            return days_overdrawn * 1.7
        base_charge = 10
        if days_overdrawn <= 7:
            return base_charge
        else:
            return base_charge + (days_overdrawn - 7) * 0.85


class NewAccount:
    def __init__(self, days_overdrawn, premium: bool) -> None:
        self._days_overdrawn = days_overdrawn
        self.type: AccountType = AccountType(premium)

    @property
    def days_overdrawn(self):
        return self._days_overdrawn

    def bank_charge(self) -> float:
        result = 4.5
        if self._days_overdrawn > 0:
            result += self.type.overdraft_charge(self._days_overdrawn)

        return result


if __name__ == "__main__":
    account = Account(3, False)
    print("Account.overdraft_charge", account.overdraft_charge)

    account = NewAccount(3, False)
    print("NewAccount.type.overdraft_charge", account.type.overdraft_charge(account.days_overdrawn))
