weight = int(input("Enter your weight(kg): "))
height = int(input("Enter your height(cm): ")) / 100
bmi = weight / (height ** 2)
if bmi < 18.5:
    print('Underweight')
elif bmi < 25 and bmi > 18.5:
    print('Normal')
elif bmi > 25:
    print('Overweight')
