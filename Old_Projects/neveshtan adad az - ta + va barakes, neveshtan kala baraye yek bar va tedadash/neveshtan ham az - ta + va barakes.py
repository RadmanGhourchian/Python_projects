x = int(input("Enter a number: "))
if x<0:
    x = -x
for i in range(-x, x + 1, 1):
    print(i)