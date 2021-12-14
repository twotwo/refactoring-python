# Chapter 10 Simplifying Conditional Logic

Refactoring: Improving the Design of Existing Code (2nd Edition)

- <https://book-refactoring2.ifmicro.com/docs/ch10.html>

## 10.1 Decompose Conditional

Motivation

- 复杂的条件逻辑是最常导致复杂度上升的地点之一
- 将它分解为多个独立的函数，经常会带来很大价值

Sketch

```python
# before
class Account:

    @property
    def overdraft_charge(self):
        ...

# after
class AccountType:
    def overdraft_charge(self, days_overdrawn):
        ...
```

Examples

- `python 801_move_function.py.py`
- [801_move_function.py.py](./801_move_function.py)

## 10.2 Consolidate Conditional Expression

Motivation

- 检查条件各不相同，最终行为却一致。如果发现这种情况，就应该使用“逻辑或”和“逻辑与”将它们合并为一个条件表达式
- 将检查条件提炼成一个独立的函数对于厘清代码意义非常有用，因为它把描述“做什么”的语句换成了“为什么这样做”

Sketch

```python
# before
@dataclass
class Customer:
    contract: CustomerContract
    discount_rate: float

# after
class Customer:
    contract: CustomerContract

    @property
    discount_rate(self):
        return contract.discount_rate()
```

Examples

- `python 802_move_field.py`
- [802_move_field.py](./802_move_field.py)

## 10.3 Replace Nested Conditional with Guard Clauses

Motivation

- 如果某个条件极其罕见，就应该单独检查该条件，并在该条件为真时立刻从函数中返回。这样的单独检查常常被称为“卫语句”（guard clauses）

Sketch

```python
# before
result.append(f"<p>title: {person.photo.title}</p>")
result.append(emit_photo_data(person.photo))

def emit_photo_data(photo: Photo):
    result = []
    result.append(f"<p>location: {photo.location}</p>")
    result.append(f"<p>date: {photo.date}</p>")
    return "\n".join(result)
# after
result.append(emit_photo_data(person.photo))

def emit_photo_data(photo: Photo):
    return "\n".join([
        f"<p>{person.name}</p>", 
        f"<p>location: {photo.location}</p>", 
        f"<p>date: {photo.date}</p>"
    ])
```

Examples

## 10.4 Replace Conditional with Polymorphism

Motivation

- 将条件逻辑拆分到不同的场景（或者叫高阶用例），从而拆解复杂的条件逻辑
- 多态是其中一种方法

Sketch

```python
# before
result.append(emit_photo_data(person.photo))

def emit_photo_data(photo: Photo):
    result = []
    result.append(f"<p>title: {person.photo.title}</p>")
    result.append(f"<p>location: {photo.location}</p>")
    return "\n".join(result)
# after
result.append(emit_photo_data(person.photo))
result.append(f"<p>location: {person.photo.location}</p>")

def emit_photo_data(photo: Photo):
    result = []
    result.append(f"<p>title: {person.photo.title}</p>")
    return "\n".join(result)
```

Examples

## 10.5 Introduce Special Case

Motivation

- 如果我发现代码库中有多处以同样方式应对同一个特殊值，我就会想要把这个处理逻辑收拢到一处

Sketch

```python
# before
applies_to_mass = False
for s in states:
    if s == "MA":
        applies_to_mass = True
# after
applies_to_mass = any(True for s in states if s == "MA")
```

## 10.6 Introduce Assertion

Motivation

- 使用断言明确标明这些保证代码正确允许的条件

Sketch

```python
# before
pricing_plan = retrieve_pricing_plan()
order = retreive_order()
charge_per_unit = pricing_plan.unit
# after
pricing_plan = retrieve_pricing_plan()
charge_per_unit = pricing_plan.unit
order = retreive_order()
```

Examples

- `python 806_slide_statements.py`
- [806_slide_statements.py](./806_slide_statements.py)
