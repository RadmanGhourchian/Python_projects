import re

National_id = input("Enter your National ID: ")
if(re.match(r"(^\d{10}$|^123\_[0-9]{6}\_\d$)", National_id)):
    print("Ok", National_id)
else:
    print("Invalid")