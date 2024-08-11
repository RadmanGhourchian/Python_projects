import re

def name_validdator(name):
    if re.match(r"^[a-zA-Z]{3,100}$", name):
        return True
    else:
        return False

def family_validdator(family):
    if re.match(r"^[a-zA-Z]{3,100}$", family):
        return True
    else:
        return False

def email_validdator(email):
    if re.match(r"^[a-zA-Z][\.\_\da-zA-Z]{1,20}\@(gmail|yahoo|msn)\.com$", email, re.I):
        return True
    else:
        return False

def national_id_validator(id):
    if (re.match(r"(^\d{10}$|^123\_[0-9]{6}\_\d$)", id)):
        return True
    else:
        return False

def phone_validator(phone):
    if re.match(r"^(09|\+989)[0-9]{9}$", phone):
        return True
    else:
        return False

def adress_validator(adress):
    if re.match(r"^[a-zA-Z\s\d\-\,\.]{1,100}$", adress):
        return True
    else:
        return False