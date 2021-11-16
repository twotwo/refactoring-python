from dataclasses import dataclass


@dataclass
class OrderBefore:
    priority: str


class Priority(object):
    def __init__(self, value) -> None:
        if type(value) == Priority:
            self.__value = str(value)
            return
        if value in Priority.legal_values():
            self.__value = value
        else:
            raise ValueError(f"{value} is invalid for Priority")

    def __repr__(self) -> str:
        return self.__value

    @property
    def index(self):
        return Priority.legal_values().index(self.__value)

    @staticmethod
    def legal_values():
        return ["low", "normal", "high", "rush"]

    def __eq__(self, o: object) -> bool:
        return self.index == o.index

    def __gt__(self, o: object) -> bool:
        return self.index > o.index

    def __lt__(self, o: object) -> bool:
        return self.index < o.index


class OrderAfter:
    def __init__(self, priority) -> None:
        self.__priority = Priority(priority)

    @property
    def priority(self):
        return self.__priority

    def __repr__(self) -> str:
        return f"OrderAfter(p={str(self.__priority)})"


if __name__ == "__main__":
    orders = [OrderBefore("low"), OrderBefore("normal"), OrderBefore("high")]
    print("more than nomal: ", [order for order in orders if order.priority == "high" or order.priority == "rash"])
    orders = [OrderAfter("low"), OrderAfter("normal"), OrderAfter("high")]
    print(orders)
    print(Priority("normal").index)
    print("more than nomal: ", [order for order in orders if order.priority > Priority("normal")])
