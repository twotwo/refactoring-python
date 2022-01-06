# Chapter 11 Refactoring APIs

Refactoring: Improving the Design of Existing Code (2nd Edition)

- <https://book-refactoring2.ifmicro.com/docs/ch11.html>

## 11.1 Separate Query from Modifier

Motivation

- 如果遇到一个“既有返回值又有副作用”的函数，试着将查询动作从修改动作中分离出来

Sketch

```python
# before
def get_total_outstanding_and_send_bill():
    result = sum([customer.invoices.amount])
    send_bill()
    return result

# after
def total_outstanding():
    return sum([customer.invoices.amount])

def send_bill():
    email_gateaway.send(format_bill(customer))
```

Examples

- [1101_separate_query_from_modifier.py](./1101_separate_query_from_modifier.py)

## 11.2 Parameterize Function

Motivation

- 将两个逻辑相似(仅有一些字面量值不同)的函数合并成一个
- 以参数的形式传入不同的值，从而消除重复

Sketch

```python
# before
def ten_percent_raise(person):
    person.salary = person.salary.multiply(1.1)


def five_percent_raise(person):
    person.salary = person.salary.multiply(1.05)


# after
def raise_salary(person, factor):
    person.salary = person.salary.multiply(1 + factor)
```

Examples

- [1102_parameterize_function.py](./1102_parameterize_function.py)

## 11.3 Remove Flag Argument

Former Name

- Replace Parameter with Explicit Methods

Motivation

- “标记参数”是这样的一种参数：调用者用它来指示被调函数应该执行哪一部分逻辑
  - 只有参数值影响了函数内部的控制流，这才是标记参数
- 移除标记参数不仅使代码更整洁，并且能帮助开发工具更好地发挥作用

```python
# before
def set_dimension(self, name, value):
    if name == "height":
        self._height = value
        return
    if name == "width":
        self._width = value
        return

# after
def set_height(self, value):
    self._height = value

def set_width(self, value):
    self._width = value
```

Examples

- [1103_remove_flag_argument.py](./1103_remove_flag_argument.py)

## 11.4 Preserve Whole Object

Motivation

- “传递整个记录”的方式能更好地应对变化
- 传递整个记录也能缩短参数列表，让函数调用更容易看懂

Sketch

```python
# before
low = room.days_temp_range.low
high = room.days_temp_range.high
assert plan.within_range(low, high)
# after
assert plan.within_range(room.days_temp_range)
```

Examples

- [1104_preserve_whole_object.py](./1104_preserve_whole_object.py)

## 11.5 Replace Parameter with Query

Former Name

- Replace Parameter with Method

Motivation

- 善用函数可以将相关的行为打包起来，有助于消除重复

Sketch

```python
# before
available_vacation(employee, employee.grade)

def available_vacation(employee, grade):
    # calculate vacation

# after
available_vacation(employee)

def available_vacation(employee):
    grade = employee.grade
    # calculate vacation
```

Examples

- [1105_replace_parameter_with_query.py](./1105_replace_parameter_with_query.py)

## 11.6 Replace Query with Parameter

Motivation

- 为了让目标函数不再依赖于某个元素，我把这个元素的值以参数形式传递给该函数
- 把“不具引用透明性的元素”变成参数传入，函数就能重获引用透明性
- 这会增加函数调用者的复杂度，需要权衡

Sketch

```python
# before
target_temperature(plan)
def target_temperature(plan):
    current_temperature = thermostat.current_temperature
    # rest of function..

# after
target_temperature(plan, thermostat.current_temperature)
def target_temperature(plan, current_temperature):
    # rest of function..
```

Examples

- [1106_replace_query_with_parameter.py](./1106_replace_query_with_parameter.py)

## 11.7 Remove Setting Method

Motivation

- 如果不希望在对象创建之后此字段还有机会被改变，那就不要为它提供设值函数

Sketch

```python
class Order(object):
    def __init__(self, id: int) -> None:
        self._id = id

    @property
    def id(self):
        return self._id
if __name__ == "__main__":
    order = Order(1)
    try:
        order.id = 2
    except AttributeError as ex:
        print("can't set attribute")
```

## 11.8 Replace Constructor with Factory Function

Motivation

- 使用工厂函数，避开构造函数局限性，如感知上下文、更清晰的函数名称和不必要的操作符等

Sketch

```python
class Worker(object):
    def __init__(self, gpu: int, heartbeat, task_buffer, service: ListNode = None):
        ...

    @staticmethod
    def create_worker(gpu: int, worker: Worker = None):
        worker = Worker(
            gpu=gpu,
            heartbeat=mp.Value("i", int(time.time())),  # int type
            task_buffer=worker.task_buffer if worker else mp.Manager().dict(),
            service=worker.current_service if worker else None,
        )
        return worker

```

## 11.9 Replace Function with Command

Motivation

- 将函数封装成自己的对象，有时也是一种有用的办法
- 与普通的函数相比，命令对象提供了更大的控制灵活性和更强的表达能力。除了函数调用本身，命令对象还可以支持附加的操作
  - 例如撤销操作
  - 支持更丰富的生命周期管理能力

Sketch

```python
# before
def score(candidate, medical_exam, scoring_guide): 
    result = 0
    health_level = 0
    # long body code

# after
class Scorer:
    def __init__(self, candidate, medical_exam, scoring_guide):
        self._candidate = candidate
        self._medical_exam = medical_exam 
        self._scoring_guide = scoring_guide

    def execute(self):
        self._result = 0
        self._health_level = 0
        # long body code
```

Examples

- [1109_replace_function_with_command.py](./1109_replace_function_with_command.py)

## 11.10 Replace Command with Function

Motivation

- 对于不是太复杂的函数，就应该考虑将其变回普通的函数

Sketch

```python
class ChargeCalculator:
    def __init__(self, customer, usage) -> None:
        self._customer = customer
        self._usage = usage
    
    def execute(self):
        return self._customer.rate * self._usage

# after
def charge(customer, usage):
    return customer.rate * usage
```

Examples

- [1110_replace_command_with_function.py](./1110_replace_command_with_function.py)
