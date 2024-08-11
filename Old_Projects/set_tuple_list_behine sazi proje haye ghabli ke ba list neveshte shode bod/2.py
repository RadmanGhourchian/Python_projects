name_list = []
name_list_less_5 = []
name_list_more_5 = []

while (name := input("Enter your name: ").lower()) != "exit":
    name_list.append(name)

for i in name_list:
    if len(i) <= 5:
        name_list_less_5.append(i)
    else:
        name_list_more_5.append(i)

print("Names more than 5 characters : ", name_list_more_5)
print("Names less than 5 characters : ", name_list_less_5)