list = []

while (product := input("Enter product name: ").lower()) != "exit":
    list.append(product)


for i in set(list):
    print(i, "-->", list.count(i))