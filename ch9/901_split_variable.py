"""
901_split_variable.py
计算一个苏格兰布丁运动的距离。

在起点处，静止的苏格兰布丁会受到一个初始力的作用而开始运动。
一段时间后，第二个力作用于布丁，让它再次加速。
根据牛顿第二定律，可以用以下的方式计算布丁运动的距离。


范例2 对输入参数赋值
"""
from dataclasses import dataclass


@dataclass
class Scenario:
    primary_force: float  # newton
    mass: float  # kilogram
    delay: float  # second
    secondary_force: float  # newton


def distance_travelled(scenario: Scenario, time: float):
    acc = scenario.primary_force / scenario.mass
    primary_time = min(time, scenario.delay)
    result = 0.5 * acc * primary_time * primary_time
    secondary_time = time - scenario.delay
    if secondary_time > 0:
        primary_velocity = acc * scenario.delay
        acc = (scenario.primary_force + scenario.secondary_force) / scenario.mass  # second acceleration
        result += primary_velocity * secondary_time + 0.5 * acc * secondary_time * secondary_time
    return result


def new_distance_travelled(scenario, time):
    primary_acceleration = scenario.primary_force / scenario.mass
    primary_time = min(time, scenario.delay)
    result = 0.5 * primary_acceleration * primary_time * primary_time
    secondary_time = time - scenario.delay
    if secondary_time > 0:
        primary_velocity = primary_acceleration * scenario.delay
        secondary_acceleration = (scenario.primary_force + scenario.secondary_force) / scenario.mass
        result += primary_velocity * secondary_time + 0.5 * secondary_acceleration * secondary_time * secondary_time
    return result


def discount(input_value, quantity):
    if input_value > 50:
        input_value -= 2
    if quantity > 100:
        input_value -= 1
    return input_value


def new_discount(input_value, quantity):
    result = input_value
    if input_value > 50:
        result -= 2
    if quantity > 100:
        result -= 1
    return result


if __name__ == "__main__":
    s = Scenario(0.3, 1, 0.5, 0.6)
    print("origin", distance_travelled(s, 0.7))
    print("new", new_distance_travelled(s, 0.7))
    assert distance_travelled(s, 0.7) == new_distance_travelled(s, 0.7)
    assert discount(80, 20) == new_discount(80, 20)
