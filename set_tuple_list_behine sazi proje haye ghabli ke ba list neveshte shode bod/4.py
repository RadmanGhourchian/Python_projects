list = []

name = input("Enter your name: ")

while (name.lower()) != "exit":
    list.append(name.capitalize())
    name = input("Enter your name: ")

list.sort()
print(list)