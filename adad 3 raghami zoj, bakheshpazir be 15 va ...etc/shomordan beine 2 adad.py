a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a>b:
    for i in range(a, b-1, -1):
        print(i)
else:
    for i in range(a , b+1, +1):
        print(i)