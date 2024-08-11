a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a>b:
    a,b = b,a
for i in range(a,b+1):
    print(i)