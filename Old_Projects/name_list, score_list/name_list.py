import re

name_list = []

name = input("Enter your name: ")
while not re.match(r"^exit$", name, re.I):
    name = name.capitalize()
    name_list.append(name)
    name = input("Enter your name: ")


name_list.sort()
print("Your name_list is :", name_list)