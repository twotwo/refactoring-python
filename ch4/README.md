# Chapter 4 Building Tests

Refactoring: Improving the Design of Existing Code (2nd Edition)

- <https://book-refactoring2.ifmicro.com/docs/ch4.html>
- [Tips in this chapter](https://medium.com/@rsolismelo/refactoring-chapter-4-building-tests-9073726c6e27)

If you want to refactor, the essential precondition is having solid tests. Even if you are fortunate enough to have a tool that can automate the refactorings, you still need tests. It will be a long time before all possible refactorings can be automated in a refactoring tool.

I don’t see this as a disadvantage. I’ve found that writing good tests greatly speeds my programming, even if I’m not refactoring. This was a surprise for me, and it is counterintuitive for many programmers, so it’s worth explaining why.

## 4.1 The Value of Self-testing Code

1. 减少调试时间
2. 良好的工作节奏：“测试、编码、重构”的循环的节奏感可使编程工作以更加高效、有条不紊的方式开展

## 4.2 Sample Code to Test

这块业务逻辑代码涉及两个类：

- `Producer` 代表一个生产商
  - 成本（`cost`）
  - 供应的数量（`production`）
- `Province` 描述一个地区的生产计划
  - 第一行：需求量（`demand`）和采购价格（`price`）
  - 一个生产商列表 `List[Producer]`
  - 底部：产量差额（`shortfall` = demand - sum(p.production)）和总利润（`profit`）

[starting_point.py](./starting_point.py) # producer 和 province 都放到一起了，以避免交叉引用

JavaScript 代码转换过程中参考的信息

- [How do I sort a dictionary by value?](https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value)
- 《流畅的 Python》 2.7 `list.sort` 方法和内置函数 `sorted`

## 4.3 A First Test

选择测试框架： `pytest`

- 设置 `fixture`
- 使用 `assert` 风格的断言

`pytest test_1_province.py`

[test_1_province.py](./test_1_province.py)

## 4.4 Add Another Test

再添加一个测试

- 测试的目标是希望找出现在或未来可能出现的 bug
- 所以测试的重点应该是那些我最担心出错的部分，这样就能从测试工作中得到最大利益

`pytest test_2_province.py`

- [conftest.py](./conftest.py) 提取 Fixture
- [test_2_province.py](./test_2_province.py)

## 4.5 Modifying the Fixture

当对测试对象进行修改时，请确保不会污染其它测试例

`pytest test_3_change_fixture.py`

[test_3_change_fixture.py](./test_3_change_fixture.py)

## 4.6 Probing the Boundaries

用边界条件检查操作出错时软件的表现

`pytest test_4_no_producers.py`

- [conftest.py](./conftest.py) 提取 Fixture: `no_producers`
- [test_4_no_producers.py](./test_4_no_producers.py)

## 4.7 Much More Than This

每当你遇见一个bug，先写一个测试来清楚地复现它。仅当测试通过时，才视为bug修完
