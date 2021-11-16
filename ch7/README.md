# Chapter 7 Encapsulation

Refactoring: Improving the Design of Existing Code (2nd Edition)

- <https://book-refactoring2.ifmicro.com/docs/ch7.html>
- [Python 重载运算符](https://segmentfault.com/a/1190000013456795)

## 7.1 Encapsulate Record

Motivation

- 让数据结构变得更加直观，更好的应对变化

Sketch

```python
# before
organization = {"name": "Acme Gooseberries", "country": "GB"}

# after
@dataclass
class Organization():
    name: str
    country: str
```

Examples

- `python 701_encapsulate_record.py`
- [701_encapsulate_record.py](./701_encapsulate_record.py)

## 7.2 Encapsulate Collection

Motivation

- 不要在模块以外修改集合

Sketch

```python
@dataclass
class Person:
    courses: List[str]

    def add_course(self, course: str):
        self.courses.append(course)

    def remove_course(self, course: str):
        self.courses.remove(course)
```

Examples

## 7.3 Replace Primitive with Object

Motivation

- 对某个数据的操作不仅仅局限于打印时，请为它创建一个新类

Sketch

```python
# before
[order for order in orders if order.priority == "high" or order.priority == "rash"]
# after
[order for order in orders if order.priority > Priority("normal")]
```

Examples

- `python 703_replace_primitive_with_object.py`
- [703_replace_primitive_with_object.py](./703_replace_primitive_with_object.py)

## 7.4 Replace Temp with Query

Motivation

- 函数的封装能力比变量强，改用函数还能避免在多个函数中重复编写计算逻辑

Sketch

```python
def before(order):
    base_price = order._quantity * order._item_price
    if base_price > 1000:
        return base_price * 0.95


def after(order):
    def base_price():
        return order._quantity * order._item_price
    if base_price() > 1000:
        return base_price() * 0.95
```

## 7.5 Extract Class

Motivation

- 一个类应该是一个清晰的抽象，只处理一些明确的责任

Sketch

```python
# before
@dataclass
class Soldier:
    health: int = 0
    damage: int = 0
    weaponStatus: int = 0

# after
@dataclass
class Weapon:
    damage: int = 0
    weaponStatus: int = 0


@dataclass
class Soldier:
    health = 0
    weapon = Weapon()
```

Examples

- `python 705_extract_class.py`
- [705_extract_class.py](./705_extract_class.py)

## 7.6 Inline Class

Motivation

- 当一个类不再承担足够责任，不再有单独存在的理由时，可以把它塞到另外一个类中

## 7.7 Hide Delegate

Motivation

- “封装”意味着每个模块都应该尽可能少了解系统的其他部分

Sketch

```python
# before
manager = person.department.manager
# after
manager = person.manager
```

Examples

## 7.8 Remove Middle Man

Motivation

- 让客户直接调用受托类

## 7.9 Substitute Algorithm

Motivation

- 用比较清晰的方式取代复杂的方式

Sketch

```python
def found_person_before(people):
    for i in range(len(people)):
        if people[i] == "Don":
            return "Don"
        if people[i] == "John":
            return "John"
        if people[i] == "Kent":
            return "Kent"
    return ""


def found_person_after(people):
    candidates = ["Don", "John", "Kent"]
    for i in range(len(people)):
        if people[i] in candidates:
            return people[i]
    return ""
```

Examples

- `python 709_substitute_algorithm.py`
- [709_substitute_algorithm.py](./709_substitute_algorithm.py)
