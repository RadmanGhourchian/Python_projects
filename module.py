import re

def model(model):
    return bool(re.match(r"^[a-zA-Z\s\d]{3,25}$", model))