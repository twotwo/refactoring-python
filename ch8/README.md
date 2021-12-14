# Chapter 8 Moving Features

Refactoring: Improving the Design of Existing Code (2nd Edition)

- <https://book-refactoring2.ifmicro.com/docs/ch8.html>

## 8.1 Move Function

Motivation

- 任何函数都需要具备上下文环境才能存活，类作为最主要的模块化手段，其本身就能充当函数的上下文
- 搬移函数最直接的一个动因是，它频繁引用其他上下文中的元素，而对自身上下文中的元素却关心甚少
- 让函数去与那些更亲密的元素相会，通常能取得更好的封装效果，因为在别的地方减少了对当前模块的依赖

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

## 8.2 Move Field

Motivation

- 数据结构是一个健壮程序的根基
- 数据结构已经不适应于需求，就应该马上修缮它。如果容许瑕疵存在并进一步累积，它们就会经常使我困惑，并且使代码愈来愈复杂

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

## 8.3 Move Statements into Function

是 8.4 `搬移语句到调用者` 的反向重构

Motivation

- 将语句搬移到函数里去，使其在一起更像一个整体，从而提升可理解性

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
        f"<p>{photo.title}</p>", 
        f"<p>location: {photo.location}</p>", 
        f"<p>date: {photo.date}</p>"
    ])
```

Examples

- `python 803_move_statements_into_function.py`
- [803_move_statements_into_function.py](./803_move_statements_into_function.py)

## 8.4 Move Statements to Callers

是 8.3 `搬移语句到函数` 的反向重构

Motivation

- 分离关注点：把表现不同的行为从函数里挪出，并搬移到其调用处
  - 以往在多个地方共用的行为，如今需要在某些调用点面前表现出不同的行为
- 这个重构手法比较适合处理边界仅有些许偏移的场景

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

- `python 804_move_statements_to_caller.py`
- [804_move_statements_to_caller.py](./804_move_statements_to_caller.py)

## 8.5 Replace Inline Code with Function Call

Motivation

- 善用函数可以将相关的行为打包起来，有助于消除重复

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

## 8.6 Slide Statements

Motivation

- 让存在关联的东西一起出现，可以使代码更容易理解

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

## 8.7 Split Loop

Motivation

- 让一个循环只做一件事情，那就能确保每次修改时你只需要理解要修改的那块代码的行为就可以了

Sketch

```python
# before
youngest = 100
total_salary = 0

for p in info:
    if p.age < youngest:
        youngest = p.age
    total_salary += p.salary
# after
youngest = 100
for p in info:
    if p.age < youngest:
        youngest = p.age

total_salary = 0
for p in info:
    total_salary += p.salary
```

Examples

- `python 807_split_loop.py`
- [807_split_loop.py](./807_split_loop.py)

## 8.8 Replace Loop with Pipeline

Motivation

- 集合管道（collection pipeline）是这样一种技术，它允许我使用一组运算来描述集合的迭代过程，其中每种运算接收的入参和返回值都是一个集合
- 采用集合管道来编写，代码的可读性会更强——我只消从头到尾阅读一遍代码，就能弄清对象在管道中间的变换过程

Sketch

```python
# before
names = []
for i in input:
    if i["job"] == "programmer":
        names.append(i["name"])
# after
names = [i["name"] for i in input if i["job"] == "programmer"]
```

Examples

- `python 808_replace_loop_with_pipeline.py`
- [808_replace_loop_with_pipeline.py](./808_replace_loop_with_pipeline.py)

## 8.9 Remove Dead Code

Motivation

- 无用代码确实会带来很多额外的思维负担
- 一旦代码不再被使用，我们就该立马删除它

Sketch

```python
# remove below code
if False:
    do_something_that_used_to_matter()
```
