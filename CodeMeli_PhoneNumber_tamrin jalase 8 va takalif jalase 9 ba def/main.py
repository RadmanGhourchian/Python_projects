from university_module import *

lessons_list_2 = []

while (add := input("Enter y for continuing : ").lower()) == "y":
    lessons = get_lessons()

    if total_units(lessons_list_2) + lessons["unit"] <= 17:
        lessons_list_2.append(lessons)
    else:
        print("invalid!")

    if total_units(lessons_list_2) == 17:
        break

print("-------------------------------------------------")
printer(lessons_list_2)