import re

email = input('Enter your email: ')
if re.match(r"^[a-zA-Z][\.\_\da-zA-Z]{1,20}\@(gmail|yahoo|msn)\.com$", email, re.I):
    print("Ok, your email is: ", email)
else:
    print("invalid")
