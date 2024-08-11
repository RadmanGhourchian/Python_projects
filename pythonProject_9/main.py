from module import *

person_list = []
male_list = []
female_list = []


while (add := input("Enter (y) for cntinueing : ").lower()) == "y":
    name = input("Enter your name: ")
    gender = input("Enter your gender (m for male and f for female): ")
    if gender_checker(gender) == False:
        print("We don't have that type of gender!")
        continue

    person = {"name": name, "gender": gender}
    person_list.append(person)


male_list = list(filter(lambda i: i["gender"] == "m", person_list))
female_list = list(filter(lambda i: i["gender"] == "f", person_list))

print("-----------------------------------------")
print("The male people are : ", male_list)
print("The female people are : ", female_list)