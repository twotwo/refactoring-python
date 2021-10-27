from typing import Dict, List, Union


class Producer(object):
    def __init__(self, province, data: Dict) -> None:
        self._province = province
        self._cost = data["cost"]
        self._name = data["name"]
        self._production = data["production"] or 0

    def set_production(self, amount: Union[str, int]):
        production = int(amount) if str == type(amount) else amount
        self._province._total_production += production - self._production
        self._production = production

    @property
    def cost(self):
        return self._cost

    @property
    def production(self):
        return self._production


class Province(object):
    def __init__(self, doc: Dict) -> None:
        self._name = doc["name"]
        self._producers: List[Producer] = []
        self._total_production = 0
        self._demand = doc["demand"]
        self._price = doc["price"]
        for p in doc["producers"]:
            self.add_producer(Producer(self, p))

    def add_producer(self, arg: Producer):
        self._producers.append(arg)
        self._total_production += arg.production

    def set_demand(self, demand: int):
        self._demand = demand

    @property
    def producers(self):
        return self._producers

    @property
    def shortfall(self):
        return self._demand - self._total_production

    @property
    def profit(self):
        return self.demand_value - self.demand_cost

    @property
    def demand_value(self):
        return self.satisfied_demand * self._price

    @property
    def satisfied_demand(self):
        return min(self._demand, self._total_production)

    @property
    def demand_cost(self):
        remaining_demand = self._demand
        result = 0
        for p in sorted(self._producers, key=lambda item: item.cost):
            contribution = min(remaining_demand, p.production)
            remaining_demand -= contribution
            result += contribution * p.cost
        return result
