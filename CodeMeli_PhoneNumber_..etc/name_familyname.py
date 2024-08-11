import re

name = input("Enter your name:")
family_name = input("Enter your family name:")
name = name.strip()
family_name = family_name.strip()
if re.match(r"^[a-zA-Z\s]{3,30}$", name) and re.match(r"^[a-zA-Z\s]{3,30}$", family_name):
    print("ok", name + " " + family_name)
else:
    print("Invalid")
