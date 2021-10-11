# Refactoring: Improving the Design of Existing Code (2nd Edition)

## Chapter 1 Refactoring: A First Example

- <https://book-refactoring2.ifmicro.com/docs/ch1.html>
- [Tips in this chapter](https://medium.com/@emaleavil/refactoring-a-first-example-32a2709c82b8)
- [Refactoring: This class is too large](https://martinfowler.com/articles/class-too-large.html) by Martin Fowler, April 2020

### 1.1 The Starting Point

`python starting_point.py`

- [plays.json](./data/plays.json)
- [invoices.json](./data/invoices.json)
- [starting_point.py](./starting_point.py)

### 1.2 Comments on the Starting Program

变化带来的挑战

- 输出格式，详单支持更多格式，例如 HTML 等
- 分类规则，剧团会开发更多的表演类型，如 历史剧、田园剧、田园喜剧、田园史剧、历史悲剧 等等
- 计费规则，支持对不同剧目和不同的营销策略等

很难找到修改点：难以了解做出的修改与现有代码如何协作实现我想要的行为。

如果程序杂乱无章，先为它整理出结构来，再做需要的修改，通常来说更加简单。

### 1.3 The First Step in Refactoring

重构的第一个步骤永远相同：首先确保即将修改的代码拥有一组可靠的测试。

构筑测试体系对重构非常重要，降低了过程中犯错的概率。

而一旦你着手写单元测试，就会发现现有的函数对测试并不友好，这也是要在后续的重构中需要解决的问题。

### 1.4 Decomposing the statement Function

拆解长函数的方法，从整个函数中分离出不同的关注点。

`statement()` 是一个计算戏剧演出费用的函数。

这里我们会用到 6.1-提炼函数（106）

- 首先从中提取出 `amount_for(perf, play)`
- 继续提炼 `play_for(perf)`
- 提炼 `volume_credits_for(perf)`

过多的临时变量会带来麻烦，接下来我们应用 7.4-以查询取代临时变量

- 提炼 `format(amount)`

接下来重构目标是 `volume_credits_for`。处理这个变量更加微妙，因为它是在循环的迭代过程中累加得到的。

- 第 1 步，就是应用 8.7-拆分循环（227）将 `volume_credits_for` 的累加过程分离出来；
- 第 2 步，使用 8.6-移动语句（223）将累加变量的声明与累加过程集中到一起；
- 第 3 步，使用 6.1-提炼函数（106）提炼出计算总数的函数；
- 第 4 步，使用 6.2-内联变量（123）完全移除中间变量

### 1.5 Status: Lots of Nested Functions

现在代码结构已经好多了。顶层的statement函数现在只剩 7 行代码，而且它处理的都是与打印详单相关的逻辑。与计算相关的逻辑从主函数中被移走，改由一组函数来支持。每个单独的计算过程和详单的整体结构，都因此变得更易理解了。

`python nested_functions.py`

- [nested_functions.py](./nested_functions.py)

```python
def statement(invoice, plays):
  def total_amount()
  def total_volume_credits()
  def locale_currency(account)
  def volume_credits_for(perf)
  def play_for(perf)
  def amount_for(perf)

  result = f"Statement for {invoice['customer']}\n"
  for perf in invoice["performances"]:
    result += f"{play_for(perf)['name']}: {locale_currency(amount_for(perf))} ({perf['audience']} seats)\n"

  result += f"Amount owed is {locale_currency(total_amount())}\n"
  result += f"You earned {total_volume_credits()} credits\n"
  return result
```

### 1.6 Splitting the Phases of Calculation and Formatting

为实现同样的计算函数可以被文本版详单和HTML版详单共用，希望将计算逻辑和渲染逻辑拆分成 2 部分

创建一个对象，作为在两个阶段间传递的中转数据结构，然后将它作为第一个参数传递给 `render_plain_text`

### 1.7 Status: Separated into Two Files(and Phases)

```python
def statement(invoice, plays):
    return render_plain_text(create_statement_data(invoice, plays))
```

### 1.8 Reorganizing the Calculations by Type

用多态的结构来实现“计算逻辑的差异是由类型代码确定”。

先建立一个继承体系，它有“喜剧”（comedy）和“悲剧”（tragedy）两个子类，子类各自包含独立的计算逻辑。调用者通过调用一个多态的amount函数，让语言帮你分发到不同的子类的计算过程中。

10.4-以多态取代条件表达式（272），将多个同样的类型码分支用多态取代。重构手法可以分成 2 步：

- 将函数搬移进 Calculator 类
- 使 PerformanceCalculator 表现出多态性(拆分出 ComedyCalculator/TragedyCalculator)

### 1.9 Status: Creating the Data with the Polymorphic

`python statement.py`

- [statement.py](./statement.py)
- [create_statement_data.py](./create_statement_data.py)

新结构带来的好处是，不同戏剧种类的计算各自集中到了一处地方。如果大多数修改都涉及特定类型的计算，像这样按类型进行分离就很有意义。当添加新剧种时，只需要添加一个子类，并在创建函数中返回它。

### 1.10 Final Thoughts

本章的重构有3个较为重要的节点，分别是

- 1.4 将 `statement` 函数分解成一组嵌套的函数
- 1.6 拆分计算逻辑和渲染逻辑
- 1.8 引入多态性来处理计算逻辑

每一步都给代码添加了更多的结构，更好的表达代码的意图。

好代码的检验标准就是人们是否能轻而易举地修改它。

关键的心得是：

- 小的步子可以更快前进
- 请保持代码永远处于可工作状态
- 小步修改累积起来也能大大改善系统的设计
