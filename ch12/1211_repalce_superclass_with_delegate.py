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


# 9.5-将值对象改为引用对象


class Scroll(object):
    """重构手法
    1. 首先给 Scroll 上添加 id
    2. 传入 CatalogItem 实例
    """

    def __init__(self, id, date_last_cleaned, catalog_id, catalog) -> None:
        self._id = id  # 1
        self._catalog_item = catalog.get(catalog_id)  # 2
        self._last_cleaned = date_last_cleaned

    @property
    def id(self):
        return self._id  # 1

    @property
    def title(self):
        return self._catalog_item._title

    def has_tag(self, arg):
        return arg in self._catalog_item._tags

    def needsCleaning(self, targetDate):
        threshold = 700 if self.has_tag("revered") else 1500
        return self.daysSinceLastCleaning(targetDate) > threshold

    def daysSinceLastCleaning(self, targetDate):
        return self._lastCleaned.until(targetDate, "UNIT_DAYS")
