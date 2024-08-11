list1 = []
for i in range(3):
    name = input("Enter your name : ")
    list1.append(name)

more_5_characters = list(map(lambda i: len(i), list1))
print(more_5_characters)