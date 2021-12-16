"""
1004_replace_conditional_with_polymorphism.py

范例2 用多态处理变体逻辑。表达某个对象与另一个对象大体类似，但又有一些不同之处。

有一家评级机构，要对远洋航船的航行进行投资评级。这家评级机构会给出“A”或者“B”两种评级，取决于多种风险和盈利潜力的因素。
在评估风险时，既要考虑航程本身的特征，也要考虑船长过往航行的历史。
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Voyage:
    zone: str
    length: int


@dataclass
class History:
    data: List[Record]

    @property
    def length(self):
        return len(self.data)

    @dataclass
    class Record:
        zone: str
        profit: int


def rating(voyage: Voyage, history: History):
    vpf = voyageProfitFactor(voyage, history)
    vr = voyageRisk(voyage)
    chr = captainHistoryRisk(voyage, history)
    if vpf * 3 > (vr + chr * 2):
        return "A"
    return "B"


def voyageRisk(voyage):
    result = 1
    if voyage.length > 4:
        result += 2
    if voyage.length > 8:
        result += voyage.length - 8
    if voyage.zone in ["china", "east-indies"]:
        result += 4
    return max(result, 0)


def captainHistoryRisk(voyage, history: History):
    result = 1
    if history.length < 5:
        result += 4
    result += len([r for r in history.data if r.profit < 0])
    if voyage.zone == "china" and hasChina(history):
        result -= 2
    return max(result, 0)


def hasChina(history):
    return any(True for r in history.data if r.zone == "china")


def voyageProfitFactor(voyage, history: History):
    result = 2
    if voyage.zone == "china":
        result += 1
    if voyage.zone == "east-indies":
        result += 1
    if voyage.zone == "china" and hasChina(history):
        result += 3
        if history.length > 10:
            result += 1
        if voyage.length > 12:
            result += 1
        if voyage.length > 18:
            result -= 1
    else:
        if history.length > 8:
            result += 1
        if voyage.length > 14:
            result -= 1
    return result


# ================= 6.9 Combine Functions into Class
def rating_stage1(voyage: Voyage, history: History):
    return Rating(voyage, history).value


class Rating:
    def __init__(self, voyage: Voyage, history: History) -> None:
        self._voyage = voyage
        self._history = history

    @property
    def value(self):
        vpf = self.voyageProfitFactor()
        vr = self.voyageRisk()
        chr = self.captainHistoryRisk()
        if vpf * 3 > (vr + chr * 2):
            return "A"
        return "B"

    @property
    def voyageRisk(self):
        result = 1
        if self._voyage.length > 4:
            result += 2
        if self._voyage.length > 8:
            result += self._voyage.length - 8
        if self._voyage.zone in ["china", "east-indies"]:
            result += 4
        return max(result, 0)

    @property
    def captainHistoryRisk(self):
        result = 1
        if self._history.length < 5:
            result += 4
        result += len([r for r in self._history.data if r.profit < 0])
        if self._voyage.zone == "china" and hasChina(self._history):
            result -= 2
        return max(result, 0)

    @property
    def voyageProfitFactor(self):
        result = 2
        if self._voyage.zone == "china":
            result += 1
        if self._voyage.zone == "east-indies":
            result += 1
        if self._voyage.zone == "china" and hasChina(self._history):
            result += 3
            if self._history.length > 10:
                result += 1
            if self._voyage.length > 12:
                result += 1
            if self._voyage.length > 18:
                result -= 1
        else:
            if self._history.length > 8:
                result += 1
            if self._voyage.length > 14:
                result -= 1
        return result

    @property
    def hasChinaHistory(self):
        return any(True for r in self._history.data if r.zone == "china")


# 另建一个空的子类，用来安放与超类不同的行为
class ExperiencedChinaRating(Rating):
    pass


# 建立一个工厂函数，在需要时返回变体类
def create_rating(voyage: Voyage, history: History):
    if voyage.zone == "china" and any(True for r in history.data if r.zone == "china"):
        return ExperiencedChinaRating(voyage, history)

    return Rating(voyage, history)


def rating_stage2(voyage: Voyage, history: History):
    # return Rating(voyage, history).value
    return create_rating(voyage, history).value


class ExperiencedChinaRating(Rating):
    @property
    def captainHistoryRisk(self):
        result = super().captainHistoryRisk - 2
        return max(result, 0)


# 分离voyageProfitFactor函数中的变体行为，首先应用 6.1 Extract Function


class NewRating:
    @property
    def voyageProfitFactor(self):
        result = 2
        if self._voyage.zone == "china":
            result += 1
        if self._voyage.zone == "east-indies":
            result += 1

        result += self.voyageAndHistoryLengthFactor

        return result

    @property
    def voyageAndHistoryLengthFactor(self):
        result = 0
        if self._voyage.zone == "china" and hasChina(self._history):
            result += 3
            if self._history.length > 10:
                result += 1
            if self._voyage.length > 12:
                result += 1
            if self._voyage.length > 18:
                result -= 1
        else:
            if self._history.length > 8:
                result += 1
            if self._voyage.length > 14:
                result -= 1
        return result


class ExperiencedChinaRating(Rating):
    @property
    def voyageAndHistoryLengthFactor(self):
        result = 0
        result += 3
        if self._history.length > 10:
            result += 1
        if self._voyage.length > 12:
            result += 1
        if self._voyage.length > 18:
            result -= 1
        return result


# 拆分这个包含 `and` 的函数 voyageAndHistoryLengthFactor 6.1 Extract Function


class NewRating:
    @property
    def voyageAndHistoryLengthFactor(self):
        result = 0
        result += self.historyLengthFactor
        if self._voyage.length > 14:
            result -= 1
        return result

    @property
    def historyLengthFactor(self):
        return 1 if self._history.length > 8 else 0


class ExperiencedChinaRating(Rating):
    @property
    def voyageAndHistoryLengthFactor(self):
        result = 0
        result += 3
        result += self.historyLengthFactor
        if self._voyage.length > 12:
            result += 1
        if self._voyage.length > 18:
            result -= 1
        return result

    @property
    def historyLengthFactor(self):
        return 1 if self._history.length > 10 else 0


# 8.4 Move Statements to Callers && 6.5 Change Function Declaration

class NewRating:
    @property
    def voyageProfitFactor(self):
        result = 2
        if self._voyage.zone == "china":
            result += 1
        if self._voyage.zone == "east-indies":
            result += 1

        result += self.historyLengthFactor
        result += self.voyageLengthFactor

        return result

    @property
    def voyageLengthFactor(self):
        return -1 if self._voyage.length > 14 else 0

    @property
    def historyLengthFactor(self):
        return 1 if self._history.length > 8 else 0


class ExperiencedChinaRating(Rating):
    @property
    def voyageLengthFactor(self):
        result = 0
        result += 3
        # result += self.historyLengthFactor
        if self._voyage.length > 12:
            result += 1
        if self._voyage.length > 18:
            result -= 1
        return result

    @property
    def historyLengthFactor(self):
        return 1 if self._history.length > 10 else 0