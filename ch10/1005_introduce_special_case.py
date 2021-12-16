"""
1005_introduce_special_case.py

范例 一家提供公共事业服务的公司将自己的服务安装在各个场所（site）
范例2 使用对象字面量（literal object） 只读逻辑下的简化 -- Python 可以用 namedtuple
范例3 使用变换
"""
from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    billing_plan: str


class Site:
    def __init__(self, customer: Customer) -> None:
        self._customer = customer  # 一个场所会对应一个顾客，当顾客不存在时填写 "unknown"

    @property
    def customer(self):
        return self._customer


class Caller:
    @staticmethod
    def client1(site: Site):
        customer = site.customer
        if customer == "unknown":
            customer_name = "occupant"
        else:
            customer_name = customer.name
        return customer_name

    @staticmethod
    def client2(customer: Customer):
        plan = "basic" if customer == "unknown" else customer.billing_plan
        return plan

    @staticmethod
    def client3(customer: Customer, new_plan):
        if customer != "unknown":
            customer.billing_plan = new_plan  # enable setting


class CallerStage1:
    @staticmethod
    def is_unknown(arg):
        if not (type(arg) == Customer or arg == "unknown"):
            raise RuntimeError(f"investigate bad value: {arg}")
        return arg == "unknown"

    @staticmethod
    def client1(site: Site):
        customer = site.customer
        if CallerStage1.is_unknown(customer):
            customer_name = "occupant"
        else:
            customer_name = customer.name
        return customer_name

    @staticmethod
    def client2(customer: Customer):
        plan = "basic" if CallerStage1.is_unknown(customer) else customer.billing_plan
        return plan

    @staticmethod
    def client3(customer: Customer, new_plan):
        if not CallerStage1.is_unknown(customer):
            customer.billing_plan = new_plan  # enable setting


# ============= Stage 2 begin =============


@dataclass
class NewCustomer:
    name: str
    billing_plan: str
    unknown: bool = False


@dataclass
class UnknownCustomer:
    name: str = "occupant"
    billing_plan: str = "basic"
    unknown: bool = True


class NewSite:
    def __init__(self, customer) -> None:
        self._customer = customer  # 一个场所会对应一个顾客，当顾客不存在时填写 "unknown"

    @property
    def customer(self):
        return self._customer if not self._customer.unknown else UnknownCustomer()


class CallerStage2:
    @staticmethod
    def is_unknown(arg):
        if not (type(arg) == NewCustomer or type(arg) == NewCustomer):  # remove "unknown"
            raise RuntimeError(f"investigate bad value: {arg}")
        return arg.unknown

    @staticmethod
    def client1(site: NewSite):
        customer = site.customer
        # if CallerStage2.is_unknown(customer):
        #     customer_name = "occupant"
        # else:
        #     customer_name = customer.name
        return customer.name

    @staticmethod
    def client2(customer: NewCustomer):
        # plan = "basic" if CallerStage2.is_unknown(customer) else customer.billing_plan
        return customer.billing_plan

    @staticmethod
    def client3(customer: NewCustomer, new_plan):
        if not CallerStage2.is_unknown(customer):
            customer.billing_plan = new_plan  # enable setting
