# Chapter 6 A First Set of Refactorings

Refactoring: Improving the Design of Existing Code (2nd Edition)

- <https://book-refactoring2.ifmicro.com/docs/ch6.html>
- [Tips in this chapter](https://medium.com/@rsolismelo/refactoring-chapter-6-a-first-set-of-refactorings-3c614c78d8e9)

## 6.1 Extract Function

Motivation

- 将意图与实现分开

Sketch

```python
def print_owing_before(invoice):
    # print_banner()
    outstanding = calculate_outstanding()

    # print details
    print(f"name: {invoice.customer}")
    print(f"amount: {outstanding}")

def print_owing_after(invoice):
    # print_banner()
    outstanding = calculate_outstanding()

    def print_details(outstanding):
        print(f"name: {invoice.customer}")
        print(f"amount: {outstanding}")

    print_details(outstanding)
```

Examples

- `python 601_extract_function.py`
- [601_extract_function.py](./601_extract_function.py)

## 6.2 Inline Function

Motivation

- 去掉非必要的间接性

Sketch

```python
def get_rating_before(driver):
    return 2 if more_than_five_late_deliveries(driver) else 1


def more_than_five_late_deliveries(driver):
    return driver.number_of_late_deliveries > 5


def get_rating_after(driver):
    return 2 if driver.number_of_late_deliveries > 5 else 1
```

Examples

- `python 602_inline_function.py`
- [602_inline_function.py](./602_inline_function.py)

## 6.3 Extract Variable

Motivation

- Introduce Explaining Variable

Sketch

```python
def price_before(order: Order):
    #   price is base price - quantity discount + shipping
    return (
        order.quantity * order.item_price
        - max(0, order.quantity - 500) * order.item_price * 0.05
        + min(order.quantity * order.item_price * 0.1, 100)
    )


def price_after(order: Order):
    base_price = order.quantity * order.item_price
    quantity_discount = max(0, order.quantity - 500) * order.item_price * 0.05
    shipping = min(base_price * 0.1, 100)
    return base_price - quantity_discount + shipping
```

Examples

- `python 603_extract_variable.py`
- [603_extract_variable.py](./603_extract_variable.py)

## 6.4 Inline Variable

Motivation

- 当变量的名字并不比表达式更有意义的时候

Sketch

```python
def has_discount_before(order):
    base_p_rice = order.base_price()
    return base_p_rice > 1000


def has_discount_after(order):
    return order.base_price() > 1000
```

## 6.5 Change Function Declaration

Motivation

- Function declarations represents the joints in our software systems
- Good joints allow me to add new parts to the system easily

Sketch

```python
def circum(radius)

def circumference(radius)
```

Examples

- `python 605_change_function_declaration.py`
- [605_change_function_declaration.py](./605_change_function_declaration.py)

## 6.6 Encapsulate Variable

Motivation

- 封装能提供一个清晰的观测点，可由此监控数据的变化和使用情况
- 还可以轻松地添加数据被修改时的验证或后续逻辑

Sketch

```python
class OwnerBefore:
    def __init__(self) -> None:
        self.default_owner = PersonBefore(first_name="Martin", last_name="Fowler")


class OwnerAfter:
    def __init__(self) -> None:
        self.__default_owner_data = PersonBefore(first_name="Martin", last_name="Fowler")

    @property
    def default_owner(self) -> PersonBefore:
        return self.__default_owner_data

    def set_default_owner(self, arg: PersonBefore):
        self.__default_owner_data = arg
```

Examples

- `python 606_encapsulate_variable.py`
- [606_encapsulate_variable.py](./606_encapsulate_variable.py)

## 6.7 Rename Variable

Motivation

- 好的命名是整洁编程的核心

Sketch

```python
# before
a = height * width
# after
area = height * width
```

Examples

## 6.8 Introduce Parameter Object

Motivation

- 将数据组织成结构是一件有价值的事，这让数据项之间的关系变得明晰
- 使用新的数据结构，参数的参数列表也能缩短
- 所有使用该数据结构的函数都会通过同样的名字来访问其中的元素，从而提升代码的一致性
- 将数据结构提升为新的抽象概念，可以帮助程序员更好地理解问题域

Sketch

```python
# before
def amount_invoiced(start_date, end_date) 
def amount_received(start_date, end_date) 
def amount_overdue(start_date, end_date)
# after
def amount_invoiced(a_date_range) 
def amount_received(a_date_range) 
def amount_overdue(a_date_range)
```

Examples

- `python 608_introduce_parameter_object.py`
- [608_introduce_parameter_object.py](./608_introduce_parameter_object.py)

## 6.9 Combine Functions into Class

Motivation

- 类可以为一组函数提供共用环境，从而简化函数调用

Sketch

```python
# before
def base(reading)
def taxable_charge(arading) 
def calculate_base_charge(reading)
# after
class Reading():
    def base(self, reading)
    def taxable_charge(self, arading) 
    def calculate_base_charge(self, reading)
```

Examples

- `python 609_combine_functions_into_class.py`
- [609_combine_functions_into_class.py](./609_combine_functions_into_class.py)

## 6.10 Combine Functions into Transform

Motivation

- 为了避免计算派生数据的逻辑到处重复，用数据变换函数来收拢所有计算派生数据的逻辑

Sketch

```python
# before
def base(reading)
def taxable_charge(arading) 
def calculate_base_charge(reading)
# after
def enrich_reading(reading: dict):
    result = reading.copy()
    result["baseCharge"] = calculate_base_charge(reading)
    result["texableCharge"] = calculate_taxable_charge(reading)
    return result
```

Examples

- `python 610_combine_functions_into_transform.py`
- [610_combine_functions_into_transform.py](./610_combine_functions_into_transform.py)

## 6.11 Split Phase

Motivation

- 把一段同时处理2个任务的代码拆分成独立的模块，这样以后我就可以一个主题一个主题的处理任务了

Sketch

```python
# before
row_order = "refactoring-001 1"
price_list = {"001": 60}
order = row_order.split()
product_price = price_list[order[0].split("-")[1]]
order_price = int(order[1]) * product_price
# after
order = paser_order(row_order)
order_price = calculate_price(order, price_list)
```

Examples

- `python 611_split_phase.py`
- [611_split_phase.py](./611_split_phase.py)