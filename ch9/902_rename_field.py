"""
902_rename_field.py
范例 给字段改名。

Generally a name refers to a specific thing (distinctive name), 
a title refers to a thing that fulfills a requirement or a role (descriptive name).

https://docs.python.org/3.7/library/collections.html
"""
from collections import namedtuple  # Deprecated since version 3.3, will be removed in version 3.9


Organization = namedtuple("Organization", field_names=["name", "country"])

NewOrganization = namedtuple("NewOrganization", field_names=["title", "country"])


if __name__ == "__main__":
    organization = {"name": "Acme Gooseberries", "country": "GB"}
    org_instance = Organization(**organization)

    new_organization = {"title": "Acme Gooseberries", "country": "GB"}
    new_org_instance = NewOrganization(**new_organization)

    print("org_instance", org_instance)
    print("new_org_instance", new_org_instance)
    assert org_instance.name == new_org_instance.title
