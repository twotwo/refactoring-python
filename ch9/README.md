# Chapter 9 Organizing Data

Refactoring: Improving the Design of Existing Code (2nd Edition)

- <https://book-refactoring2.ifmicro.com/docs/ch9.html>

## 9.1 Split Variable

Previous Names

- Remove Assignments to Parameters
- Split Temp

Motivation

- 变量应该只被赋值一次

Sketch

```python
# before
def discount(input, quantity):
    if quantity > 50:
        input -= 2

# after
def discount(input, quantity):
    result = input
    if quantity > 50:
        result -= 2
```

```python
# before
temp = 2 * (height + width)
print(temp)
temp = height * width
print(temp)

#after
perimeter = 2 * (height + width)
print(perimeter)
area = height * width
print(area)
```

Examples

- [901_split_variable.py](./901_split_variable.py)

## 9.2 Rename Field

Motivation

- 数据结构是理解程序行为的关键，需要保持它们的整洁

Sketch

```python
# before
@dataclass
class Organization:
    def __init__(self):
        self.name = ...

# after
class Organization:
    def __init__(self):
        self.title = ...
```

Examples

- [902_rename_field.py](./902_rename_field.py)

## 9.3 Replace Derived Variable with Query

Motivation

- 尽量把可变数据的作用域限制在最小范围
- 朝着消除可变性的方向努力
- 两种风格的选择：数据不可变时函数式也可以；一般还是推荐对象封装

Sketch

```python
# before
class Account:
    @properties
    def discounted_total(self):
        return self._discounted_total

    def set_discount(self, discount):
        old = this._discount
        self._discount = discount
        self._discounted_total += old - discount

#after
class Account:
    @properties
    def discounted_total(self):
        return self._base_total - this._discount

    def set_discount(self, discount):
        self._discount = discount
```

Examples

- [903_replace_derived_variable_with_query.py](./903_replace_derived_variable_with_query.py)

## 9.4 Change Reference to Value

是 9.5 `值对象改为引用对象` 的反向重构

Motivation

- 判断成员变量是引用对象还是值对象，差别在于是否用新对象替换原有对象
- 值对象通常更容易理解，主要因为它们是不可变的

Sketch

```python
# before
class Product:
    def apply_discount(self, arg):
        self._price.amount -= arg

#after
class Product:
    def apply_discount(self, arg):
        self._price = Money(this._price.amount - arg, this._price.currency)
```

Examples

- [904_change_reference_to_value.py](./904_change_reference_to_value.py)

## 9.5 Change Value to Reference

是 9.4 `将引用对象改为值对象` 的反向重构

Motivation

- 共享的数据需要更新

Sketch

```python
# before
customer = Customer(customer_data)
# after
customer = customer_repository.get(customer_data.id)
```

Examples

- [905_change_value_to_reference.py](./905_change_value_to_reference.py)
