"""
1211_repalce_subclass_with_delegate.py

范例 Booking 类用于处理演出（show）的预订（booking）。
它有一个子类，专门用于预订高级（premium）票，这个子类要考虑各种附加服务（extra）。
"""
from __future__ import annotations


class Booking(object):
    def __init__(self, show, date) -> None:
        self._show = show
        self._date = date

    def _be_premium(self, extras):
        self._premium_delegate: PremiumBookingDelegate = PremiumBookingDelegate(self, extras)

    @property
    def has_talkback(self):
        return (
            self._premium_delegate.has_talkback()
            if hasattr(self, "_premium_delegate")
            else self._show.hasOwnProperty("talkback") and not self.isPeakDay
        )

    @property
    def base_price(self):
        result = self._show.price
        if self.isPeakDay:
            result += round(result * 0.15)
        return self._premium_delegate.extend_base_price(result) if hasattr(self, "_premium_delegate") else result

    @property
    def has_dinner(self):
        if not hasattr(self, "_premium_delegate"):
            raise RuntimeError("undefined method")

        return self._premium_delegate.has_dinner


# step 1: 用 11.8-以工厂函数取代构造函数，把构造函数封装起来
def create_booking(show, date):
    return Booking(show, date)


def create_premium_booking(show, date, extras):
    result = Booking(show, date)
    result._be_premium(extras)
    return result


# step2: 创建委托类，指向超类的反向引用和子类所需的数据
class PremiumBookingDelegate:
    def __init__(self, host_booking, extras) -> None:
        self._host = host_booking
        self._extras = extras

    @property
    def has_talkback(self):
        return self._host._show.hasOwnProperty("talkback")

    @property
    def extend_base_price(self, base):
        return round(base + self._extras.premiumFee)

    @property
    def has_dinner(self):
        return self._extras.hasOwnProperty("dinner") and not self.isPeakDay
