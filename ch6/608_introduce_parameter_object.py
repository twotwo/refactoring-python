station = {
    "name": "ZB1",
    "readings": [
        {"temp": 47, "time": "2016-11-10 09:10"},
        {"temp": 53, "time": "2016-11-10 09:20"},
        {"temp": 58, "time": "2016-11-10 09:30"},
        {"temp": 53, "time": "2016-11-10 09:40"},
        {"temp": 51, "time": "2016-11-10 09:50"},
    ],
}


def readings_outside_range_before(station, min, max):
    return [t for t in station["readings"] if t["temp"] < min or t["temp"] > max]


class NumberRange(object):
    def __init__(self, min, max) -> None:
        self.__min = min
        self.__max = max

    @property
    def min(self):
        return self.__min

    @property
    def max(self):
        return self.__max


def readings_outside_range_after(station, temp_range: NumberRange):
    return [t for t in station["readings"] if t["temp"] < temp_range.min or t["temp"] > temp_range.max]


if __name__ == "__main__":
    temp_range = NumberRange(50, 60)
    print(readings_outside_range_after(station, temp_range))
