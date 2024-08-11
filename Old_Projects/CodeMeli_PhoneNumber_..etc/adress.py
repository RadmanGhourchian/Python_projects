import re

adress = input("Enter your adress: ")
if re.match(r"^[a-zA-Z\s\d\-\,]{1,100}$", adress):
    print("Ok, your adress is:", adress)
else:
    print("invalid")