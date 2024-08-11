name_list = []
name_list_5 = []

while (name := input("Enter your name : ").lower()) != "exit":
    if len(name) <= 5:
        name_list_5.append(name)
    else:
        name_list.append(name)


print("Names less than 5 characters : ", name_list_5)
print("Names more than 5 characters : ", name_list)