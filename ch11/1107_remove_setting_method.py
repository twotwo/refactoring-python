"""
1107_remove_setting_method.py

Python @property 默认无法 set
"""


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
