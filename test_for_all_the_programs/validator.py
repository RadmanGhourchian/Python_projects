import re


def name_validator(name):
    if re.match(r"^[a-zA-Z\d\s]{3,30}$", name):
        return True
    else:
        return False


def brand_validator(brand):
    if re.match(r"^[a-zA-Z\s\d]{3,30}$", brand):
        return True
    else:
        return False


def product_validator(product):
    if re.match(r"^[a-zA-Z\s\d]{3,30}$", product):
        return True
    else:
        return False

def person_validator(person):
    if re.match(r"^[a-zA-Z\s\d]{3,30}$", person):
        return True
    else:
        return False