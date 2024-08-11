import re

phone_number = input('Enter your mobile number: ')
if re.match(r"^(09|\+989)[0-9]{9}$", phone_number):
    print("Ok, your number is :" + phone_number)
else:
    print("Invalid")