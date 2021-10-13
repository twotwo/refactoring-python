"""
__init__.py
chapter 1 - Refactoring: A First Example    Object for Python Sample
"""
import json
from typing import Dict, List


class Play(object):
    def __init__(self, name: str, play_type: str) -> None:
        self._name = name
        self._type = play_type

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type


class Plays(object):
    def __init__(self, data: Dict[str, Dict]) -> None:
        self._data = {id: Play(name=play["name"], play_type=play["type"]) for id, play in data.items()}

    @staticmethod
    def load_plays(json_file: str):
        with open(json_file) as f:
            data = json.load(f)
        return Plays(data)

    def get_play(self, id: str):
        return self._data[id]


class Performance(object):
    def __init__(self, play_id: str, audience: int) -> None:
        self.play_id = play_id
        self.audience = audience


class Invoice(object):
    def __init__(self, customer: str, perfs: List[Performance]) -> None:
        self._customer = customer
        self._perfs = perfs

    @property
    def customer(self):
        return self._customer

    @property
    def performances(self):
        return self._perfs

    @staticmethod
    def load_invoices(json_file: str) -> List:
        with open(json_file) as f:
            result: List[Invoice] = []
            for data in json.load(f):
                customer = data["customer"]
                perfs = [Performance(perf["playID"], perf["audience"]) for perf in data["performances"]]
                result.append(Invoice(customer, perfs))
            return result
