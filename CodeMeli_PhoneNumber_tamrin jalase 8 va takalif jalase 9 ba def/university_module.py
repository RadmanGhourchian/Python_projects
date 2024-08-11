lessons_list = []

def get_lessons():
    lessons = {
        "study_name": input("Enter the name of the lesson: "),
        "teacher_name": input("Enter the name of the teacher: "),
        "unit": float(input("Enter the count of the unit: ")),
    }
    return lessons

def total_units(lessons_list):
    total_units = 0
    for lesson in lessons_list:
        total_units = total_units + lesson["unit"]

    return total_units

def printer(lessons_list):
    for i in lessons_list:
        print("The name of your study is : ", i["study_name"])
        print("The name of your teacher is : ", i["teacher_name"])
        print("The count of unit for this lessons is : ", i["unit"])
        print("----------------------------------------------------")