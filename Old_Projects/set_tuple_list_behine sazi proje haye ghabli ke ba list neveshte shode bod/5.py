tuple_list = ()
list = list(tuple_list)

for i in range(1,11):
    number = int(input("Enter a number: "))
    list.append(number)

tuple_list = tuple(list)
avg = sum(tuple_list)/len(tuple_list)
for i in tuple_list:
    if i > avg:
        print(i)