from module import *

list_2 = []

while (add := input("Enter (y) for going on : ").lower()) == "y":
    dict_lesson = get_lesson()
    unit_sum = sum_unit()
    if unit_sum <= 17:
        list_2.append(dict_lesson)

print("-" * 40)
for i in list_2:
    print("Your study name is : ", i["study"])
    print("Your teacher's name is : ", i["teacher_name"])
    print("Your teacher's family name is : ", i["teacher_family"])
    print("Your unit is : ", i["unit"])
    if len(list_2) >= 2:
        print("-" * 40)
print("The sum of the units are : ", sum_unit())
