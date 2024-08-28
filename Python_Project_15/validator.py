import re


def product_validator(self):
    if re.match(r"^[a-zA-Z\s\d]{3,30}$", self.product):
        return True
    else:
        return False


def person_validator(self):
    if re.match(r"^[a-zA-Z\s\d]{3,30}$", self.person):
        return True
    else:
        return False