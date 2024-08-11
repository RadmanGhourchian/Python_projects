from module_2 import *

name = input("Enter your name: ")
if name_validdator(name):
    print("Name is Valid")
else:
    while name_validdator(name) != True:
        name = input("Enter your name: ")

family_name = input("Enter your family name: ")
if family_validdator(family_name):
    print("Family Name is Valid")
else:
    while family_validdator(family_name) != True:
        family_name = input("Enter your family name: ")

email = input("Enter your email: ")
if email_validdator(email):
    print("Email is Valid")
else:
    while email_validdator(email) != True:
        email = input("Enter your email: ")

national_id = input("Enter your national id: ")
if national_id_validator(national_id):
    print("National ID is Valid")
else:
    while national_id_validator(national_id) != True:
        national_id = input("Enter your national id: ")

phone_number = input("Enter your phone number: ")
if phone_validator(phone_number):
    print("Phone number is Valid")
else:
    while phone_validator(phone_number) != True:
        phone_number = input("Enter your phone number: ")

adress = input("Enter your adress: ")
if adress_validator(adress):
    print("Adress is Valid")
else:
    while adress_validator(adress) != True:
        adress = input("Enter your adress: ")