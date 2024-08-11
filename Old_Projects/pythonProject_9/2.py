from module_2 import *

lesson_list = []

while (add := input("Enter (y) for continuing : ").lower()) == "y":
    adding = adder()
    lesson_list.append(adding)


more_less_alipour(lesson_list)