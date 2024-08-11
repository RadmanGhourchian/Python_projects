def adder():
    study_name = input("Enter the study name: ")
    teacher_name_family = input("Enter the teacher name: ")
    unit = float(input("Enter the unit : "))
    lesson = {"study_name": study_name, "teacher_name": teacher_name_family, "unit": unit}
    return lesson

def more_less_alipour(lesson_list):
    more_5_unit = list(filter(lambda i: i["unit"] >= 5, lesson_list))
    less_5_unit = list(filter(lambda i: i["unit"] < 5, lesson_list))
    print("The studies more than 5 units are : ", more_5_unit)
    print("The lessons more than 5 units are : ", less_5_unit)

    print("----------------------------------------------------")

    alipour_list_more = list(filter(lambda i: i["teacher_name"] == "alipour", more_5_unit))
    alipour_list_less = list(filter(lambda i: i["teacher_name"] == "alipour", less_5_unit))

    for i in alipour_list_more:
        i.pop("teacher_name")
    for i in alipour_list_less:
        i.pop("teacher_name")
    print("The lists more than 5 units and with the name of alipour are  :", alipour_list_more)
    print("The lists less than 5 units and with the name of alipour are  :", alipour_list_less)
