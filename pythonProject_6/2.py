list = []
study_list = []
unit_list = []

while (add := input("Enter your (y) if you want to continue : ").lower()) == "y":
    study = input("Enter your study name: ")
    teacher_name = input("Enter your teacher name: ")
    teacher_family_name = input("Enter your teacher family name: ")
    teacher_dict = {"teacher_name": teacher_name, "teacher_family_name": teacher_family_name}
    unit = float(input("Enter your unit : "))
    unit_list.append(unit)
    if sum(unit_list) > 17:
        print("You don't have enough unit for that!")
        unit_list.pop()
        continue

    date = (input("Enter the year : "), input("Enter the month : "), input("Enter the day : "))
    dict_list = {"study": study, "teacher_family_name_2": teacher_dict, "unit": unit, "date": date}
    list.append(dict_list)
print("-" * 35)
for i in list:
    print("Your study name is : ", i["study"])
    print("Your teacher name is : ", i["teacher_family_name_2"]['teacher_name'])
    print("Your teacher family_name is : ", i["teacher_family_name_2"]['teacher_family_name'])
    print("Your unit is : ", i["unit"])
    if len(list) >= 2:
        print("-" * 35)

print("sum unit : ", sum(unit_list))