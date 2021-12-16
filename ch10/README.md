# Chapter 10 Simplifying Conditional Logic

Refactoring: Improving the Design of Existing Code (2nd Edition)

- <https://book-refactoring2.ifmicro.com/docs/ch10.html>

## 10.1 Decompose Conditional

Motivation

- 复杂的条件逻辑是最常导致复杂度上升的地点之一
- 将它分解为多个独立的函数，经常会带来很大价值
- 本重构手法其实只是6.1-提炼函数（106）的一个应用场景

Sketch

```python
def charge_before(plan: Plan):
    if plan.month > 6 and plan.month < 10:
        return plan.quantity * plan.summer_rate
    else:
        return plan.quantity * plan.regular_rate + plan.regular_service_charge

def charge_after(plan: Plan):
    return plan.summer_charge() if plan.summer() else plan.regular_charge()
```

Examples

- [1001_decompose_conditional.py](./1001_decompose_conditional.py)

## 10.2 Consolidate Conditional Expression

Motivation

- 检查条件各不相同，最终行为却一致。如果发现这种情况，就应该使用“逻辑或”和“逻辑与”将它们合并为一个条件表达式
- 将检查条件提炼成一个独立的函数对于厘清代码意义非常有用，因为它把描述“做什么”的语句换成了“为什么这样做”

Sketch

```python
# before
if employee.seniority < 2:
  return 0
if employee.months_disabled > 12:
  return 0
if employee.part_time:
  return 0

# after
if is_not_eligible_for_disablility(employee):
  return 0
def is_not_eligible_for_disablility(employee):
  return employee.seniority < 2 or employee.months_disabled > 12 or employee.part_time
```

Examples

- [1002_consolidate_conditional_expression.py](./1002_consolidate_conditional_expression.py)

## 10.3 Replace Nested Conditional with Guard Clauses

Motivation

- 如果某个条件极其罕见，就应该单独检查该条件，并在该条件为真时立刻从函数中返回。这样的单独检查常常被称为“卫语句”（guard clauses）

Sketch

```python
# before
def get_pay_amount(person):
    result = 0
    if person.dead:
        result = dead_amount()
    else:
        if person.seperated:
            result = seperated_amount()
        else:
            if person.retired:
                result = retired_amount()
            else:
                result = normal_pay_amount()
    return result
# after
def get_pay_amount(person):
    if person.dead:
        return dead_amount()
    if person.seperated:
        return seperated_amount()
    if person.retired:
        return retired_amount()
    return normal_pay_amount()
```

Examples

- [1003_replace_nested_conditional_with_guard_clauses.py](./1003_replace_nested_conditional_with_guard_clauses.py)

## 10.4 Replace Conditional with Polymorphism

Motivation

- 将条件逻辑拆分到不同的场景（或者叫高阶用例），从而拆解复杂的条件逻辑
- 多态是其中一种方法

Sketch

```python
# before
if bird.type == 'EuropeanSwallow':
    return "average"
if bird.type == 'AfricanSwallow':
    return "tired" if bird.number_of_coconuts > 2 else "average"
if bird.type == 'NorwegianBlueParrot':
    return "scorched" if bird.voltage > 100 else "beautiful"
return "unknown"
# after
class EuropeanSwallow:
    def plumage(self):
        return "average"

class AfricanSwallow:
    def plumage(self):
        return "tired" if self.number_of_coconuts > 2 else "average"

class NorwegianBlueParrot:
    def plumage(self):
        return "scorched" if self.voltage > 100 else "beautiful"
```

Examples

- [1004_replace_conditional_with_polymorphism.py](./1004_replace_conditional_with_polymorphism.py) # 本章最复杂的一个例子

## 10.5 Introduce Special Case

Previous Names

- Introduce Null Object

Motivation

- 如果我发现代码库中有多处以同样方式应对同一个特殊值，我就会想要把这个处理逻辑收拢到一处

Sketch

```python
# before
if customer == "unknown":
  customer_name = "occupant"

# after
class UnknownCustomer:
  @properties
  def name(self):
    return "occupant"
```

Examples

- [1005_introduce_special_case.py](./1005_introduce_special_case.py)

## 10.6 Introduce Assertion

Motivation

- 使用断言明确标明保证代码正确允许的条件
- 断言是一种很好的交流形式，对调试也有帮助

Sketch

```python
# before
if discount_rate:
    base = base - discount_rate * rate
# after
assert discount_rate >= 0
if discount_rate:
    base = base - discount_rate * rate
```

Examples

- [1006_introduce_assertion.py](./1006_introduce_assertion.py)
