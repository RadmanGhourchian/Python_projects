from module_1 import *

inf_list = []

while (add := input("Enter y for continuing : ").lower()) == "y":
    inf = get_inf()

    if thousand_dollar(inf_list) + (inf["price"] * inf["count"]) <= 1000:
        inf_list.append(inf)
        print("Your Product is addable")
        print("you only have", 1000 - (thousand_dollar(inf_list)), "much left")
    else:
        print("Your Product is not addable")
        print("You can just buy something with this price : ", 1000 - thousand_dollar(inf_list))

    if 1000 - thousand_dollar(inf_list) == 0:
        break

    print("--------------------------------------------------")


printer(inf_list)