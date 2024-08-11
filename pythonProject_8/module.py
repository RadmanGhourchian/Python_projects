list = []


def get_lesson():
    study = input("Enter your study name : ")
    teacher_name = input("Enter your teacher name: ")
    teacher_family_name = input("Enter your teacher family name: ")
    unit = float(input("Enter your unit : "))
    date = (input("Enter the year : "), input("Enter the month : "), input("Enter the day : "))
    dict_lesson = {"study": study, "teacher_name": teacher_name, "teacher_family": teacher_family_name, "date": date,
                   "unit": unit}
    # list.append(dict_lesson)
    return dict_lesson


def sum_unit():
    total_list = []
    for i in list:
        if i["unit"] + sum(total_list) <= 17:
            total_list.append(i["unit"])

    return sum(total_list)
