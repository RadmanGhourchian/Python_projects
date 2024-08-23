import re

def product_validator(product):
    if re.match(r"^[a-zA-Z\d\s]{4,40}$", product):
        return True
    else:
        return False

def person_validator(person):
    if re.match(r"^[a-zA-Z\s\_]{4,20}$", person):
        return True
    else:
        return False