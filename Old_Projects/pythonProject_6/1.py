list = []

while (add:=input('Enter a y for going on: ').lower()) == "y":
    car_name = input('Enter a car name: ')
    car_model = input('Enter a car model: ')
    car_price = int(input('Enter a car price: '))
    dict_list = {"car_name": car_name, "car_model": car_model, "car_price": car_price}
    list.append(dict_list)

print("-" * 35)
list_sum = []
print("The number of cars : ", len(list))
for i in list:
    print("          car name : ", i["car_name"], "          car model : ", i["car_model"])
    list_sum.append(i["car_price"])

print("-" * 35)
print("Sum of the prices are : ", sum(list_sum))