list1 = []
less_5_character = []

while (name := input("Enter your name : ").lower()) != "exit":
    list1.append(name)

more_5_character = list(filter(lambda i: len(i) >= 5, list1))
less_5_character = list(filter(lambda i: len(i) < 5, list1))
print("The words more than 5 characters are : ", more_5_character)
print("The words less than 5 characters are : ", less_5_character)
