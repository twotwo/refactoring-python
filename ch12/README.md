# Chapter 12 Dealing with Inheritance

Refactoring: Improving the Design of Existing Code (2nd Edition)

- <https://book-refactoring2.ifmicro.com/docs/ch12.html>

## 12.1 Pull Up Method

The Inverse

- 12.4 函数下移（Push Down Method）

Motivation

- 避免重复代码

Sketch

```python
# before
class Employee:
    pass

class Engineer(Employee):
    @property
    def name(self):
        pass

class Salesman(Employee):
    @property
    def name(self):
        pass

# after
class Employee:
    @property
    def name(self):
        pass

class Engineer(Employee):
    pass

class Salesman(Employee):
    pass
```

Examples

- [1201_pull_up_method.py](./1201_pull_up_method.py)

## 12.2 Pull Up Field

The Inverse

- 12.5 字段下移（Push Down Field）

Motivation

- 消除重复的数据声明

Sketch

```python
# before
class Employee:  # 12.4


class Engineer(Employee):
    def __init__(self, name) -> None:
        self._name = name


class Salesman(Employee):
    def __init__(self, name) -> None:
        self._name = name

# after
class Employee:
    def __init__(self, name) -> None:
        self._name = name


class Engineer(Employee):
    def __init__(self, name) -> None:
        super().__init__(name, "engineer")


class Salesman(Employee):
    def __init__(self, name) -> None:
        super().__init__(name, "salesman")
```

## 12.3 Pull Up Constructor Body

Motivation

- 构造函数的使用相比普通函数受到更多的限制
- 提炼构造函数相比提炼一般函数需要一些特殊处理；针对更为复杂的构造函数，可以使用 11.8-以工厂函数取代构造函数

```python
# before
class Party:


class Employee(Party):
    def __init__(self, name, id, monthly_cost):
        super().__init__()
        self._name = name
        self._name = id
        self._monthly_cost = monthly_cost

# after
class Party:
    def __init__(self, name) -> None:
        self._name = name


class Employee(Party):
    def __init__(self, name, id, monthly_cost):
        super().__init__(name)
        self._id = id
        self._monthly_cost = monthly_cost
```

Examples

- [1203_pull_up_constructor_body.py](./1203_pull_up_constructor_body.py)

## 12.4 Push Down Method

The Inverse

- 12.1 函数上移（Pull Up Method）

Motivation

- 超类中某个函数只与一个（或少数几个）子类有关，那么最好将其从超类中挪走，放到真正关心它的子类中去

Sketch

```python
# before
class Employee:  # 12.6
    @property
    def quata(self)


class Engineer(Employee)


class Salesman(Employee):

# after
class Employee()


class Engineer(Employee)


class Salesman(Employee):
    @property
    def quata(self)

```

## 12.5 Push Down Field

The Inverse

- 12.2 字段上移（Pull Up Field）

Motivation

- 如果某个字段只被一个子类（或者一小部分子类）用到，就将其搬移到需要该字段的子类中

Sketch

```python
# before

# after

```

## 12.6 Replace Type Code with Subclasses

The Inverse

- 12.7 移除子类（Remove Subclass）

Motivation

- 引入子类，利用继承带来两大好处
  - 首先，你可以用多态来处理条件逻辑；
  - 另外，将非全局字段和函数搬移到需要的子类中

Sketch

```python
# before
def createEmployee(name, type_code):
    return Employee(name, type_code)

# after
def createEmployee(name, type_code):
    if type_code == "engineer":
        return Engineer(name)
    if type_code == "salesman":
        return Salesman(name)
    if type_code == "manager":
        return Manager(name)
```

Examples

- [1206_replace_type_code_with_subclasses.py](./1206_replace_type_code_with_subclasses.py)

## 12.7 Remove Subclass

The Inverse

- 12.6 以子类取代类型码（Replace Type Code with Subclasses）

Motivation

- 如果子类的用处太少，就不值得存在了

Sketch

```python
# before
class Person():
    @property
    def gender_code(self):
        return "X"
class Male(Person):
    @property
    def gender_code(self):
        return "M"
class Female(Person):
    @property
    def gender_code(self):
        return "F"

# after
class Person:
    @property
    def gender_code(self):
        return self._gender_code
```

Examples

- [1207_remove_subclass.py](./1207_remove_subclass.py)

## 12.8 Extract Superclass

Motivation

- 如果两个类在做相似的事，可以利用基本的继承机制把它们的相似之处提炼到超类中
  - 很多时候，合理的继承关系是在程序演化的过程中才浮现出来的
- 把重复的行为收拢一处
  - 在继承和委托之间的选择：12.8 提炼超类 和 7.5-提炼类

Sketch

```python
# before
class Department:
    @property
    def total_annual_cost(self):
        return self._annual_cost

    @property
    def name(self):
        return self._name

    @property
    def head_count(self):
        return self._head_count


class Employee:
    @property
    def annual_cost(self):
        return self._annual_cost

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id


# after
class Party:
    @property
    def annual_cost(self):
        return self._annual_cost

    @property
    def name(self):
        return self._name


class Department(Party):
    @property
    def annual_cost(self):
        return self._annual_cost

    @property
    def head_count(self):
        return self._head_count


class Employee(Party):
    @property
    def annual_cost(self):
        return self._annual_cost

    @property
    def id(self):
        return self._id
```

## 12.9 Collapse Hierarchy

Motivation

- 当类与其超类已经没多大差别，不值得再作为独立的类存在时，把超类和子类合并起来

Sketch

```python
# before
class Employee:
    pass
class Salesman(Employee):
    pass

# after
class Employee:
    pass

```

## 12.10 Replace Subclass with Delegate

Motivation

- 对于不是太复杂的函数，就应该考虑将其变回普通的函数

Sketch

```python
# before
class Order(object):
    @property
    def days_to_ship(self):
        return self._warehouse.days_to_ship

class PriorityOrder(Order):
    @property
    def days_to_ship(self):
        return self._priority_plan.days_to_ship

# after
class Order(object):
    def __init__(self, delegate: PriorityOrderDelegate = None) -> None:
        self._priority_delegate = delegate

    @property
    def days_to_ship(self):
        return self._priority_delegate.days_to_ship if self._priority_delegate else self._warehouse.days_to_ship


class PriorityOrderDelegate:
    @property
    def days_to_ship(self):
        return self._priority_plan.days_to_ship
```

Examples

- [1210_repalce_subclass_with_delegate.py](./1210_repalce_subclass_with_delegate.py)

## 12.11 Replace Superclass with Delegate

Former Name

- 以委托取代继承（Replace Inheritance with Delegation）

Motivation

- 使用委托关系能更清晰地表达“这是另一个东西，我只是需要用到其中携带的一些功能”这层意思
- 如果符合继承关系的语义条件（超类的所有方法都适用于子类，子类的所有实例都是超类的实例），那么继承是一种简洁又高效的复用机制
  - 超类的一些函数对子类并不适用时，不应该通过继承来获得超类的功能
  - 合理的继承关系应该满足“子类的所有实例也都是超类的实例”，应避免“类型与实例名不符实”（type-instance homonym）

Sketch

```python
# before
class List(object):
    pass
class Stack(List):
    pass

# after
class Stack(object):
    def __init__(self) -> None:
        self._storage = List()
```

Examples

- [1211_repalce_superclass_with_delegate.py](./1211_repalce_superclass_with_delegate.py)
