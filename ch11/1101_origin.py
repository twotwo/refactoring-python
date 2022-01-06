"""
1101_separate_query_from_modifier.py

范例 有这样一个函数，它会遍历一份恶棍（miscreant）名单，检查一群人（people）里是否混进了恶棍。
如果发现了恶棍，该函数会返回恶棍的名字，并拉响警报。
如果人群中有多名恶棍，该函数也只汇报找出的第一名恶棍（我猜这就已经够了）。
"""


def alert_for_miscreant(people):
    for p in people:
        if p == "Don":
            set_off_alarms()
            return "Don"
        if p == "John":
            set_off_alarms()
            return "John"
    return ""


def set_off_alarms():
    print("alerm")


if __name__ == "__main__":
    people = ["Adam", "Bob", "Dan"]
    alert_for_miscreant(people)
