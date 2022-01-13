"""
1211_repalce_superclass_with_delegate.py
范例 有一座古城，城里的图书馆里存放上古卷轴（scroll）
卷轴的信息被编制了一份目录（catalog），每份卷轴都有一个ID号，并记录了卷轴的标题（title）和一系列标签（tag）。
"""


class CatalogItem(object):
    def __init__(self, id, title, tags) -> None:
        self._id = id
        self._title = title
        self._tags = tags

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    def has_tag(self, arg):
        return arg in self._tags


class Scroll(CatalogItem):
    """这些古老的卷轴需要日常清扫，因此代表卷轴的 Scroll 类
    继承了代表目录项的CatalogItem类，并扩展出与“需要清扫”相关的数据
    """

    def __init__(self, id, title, tags, date_last_cleaned) -> None:
        super().__init__(id, title, tags)
        self._last_cleaned = date_last_cleaned

    def needsCleaning(self, targetDate):
        threshold = 700 if self.has_tag("revered") else 1500
        return self.daysSinceLastCleaning(targetDate) > threshold

    def daysSinceLastCleaning(self, targetDate):
        return self._lastCleaned.until(targetDate, "UNIT_DAYS")


# 这就是一个常见的建模错误。真实存在的卷轴和只存在于纸面上的目录项，是完全不同的两种东西:
# 因为有很多同名的卷轴，目录上的一个名字会对应多个卷轴的
# 把“目录项”作为“卷轴”的超类很可能会把未来的程序员搞迷糊，这是一个糟糕的模型


class Scroll(object):  # 3
    """重构手法
    1. 创建一个属性，令其指向一个新建的CatalogItem实例
    2. 所有属于超类的函数，逐一为它们创建转发函数
    3. 去除Scroll与CatalogItem之间的继承关系
    """

    def __init__(self, id, title, tags, date_last_cleaned) -> None:
        # super().__init__(id, title, tags) # 3
        self._catalogItem = CatalogItem(id, title, tags)  # 1
        self._last_cleaned = date_last_cleaned

    @property
    def id(self):  # 2
        return self._catalogItem._id

    @property
    def title(self):  # 2
        return self._catalogItem._title

    def has_tag(self, arg):  # 2
        return arg in self._catalogItem._tags

    def needsCleaning(self, targetDate):
        threshold = 700 if self.has_tag("revered") else 1500
        return self.daysSinceLastCleaning(targetDate) > threshold

    def daysSinceLastCleaning(self, targetDate):
        return self._lastCleaned.until(targetDate, "UNIT_DAYS")
