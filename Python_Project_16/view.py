from classes import *
from database import *

product_list = []
product_list_2 = []

while (add := input("Enter (y) for continuing : ").lower()) == "y":
    product = input("Enter your product name : ")
    product_list.append(product)
    print(product_list)
    elec_unelec = input("Enter electric if your product is electric or if it isn't type unelectric: ").lower()
    product_list.append(elec_unelec)
    print(product_list)
    if elec_unelec == "electric":
        elec_type = input("Is it Laptop or Mobile or Monitor: ").lower()
        product_list.append(elec_type)
        print(product_list)
        if elec_type == "mobile":
            mobile_model = input("Is it Samsung or Apple : ").lower()
            product_list.append(mobile_model)
            print(product_list)
            if mobile_model == "samsung":
                samsung_price = float(input("Enter the price : "))
                samsung_weight = input("Enter the weight : ")
                samsung_voltage = input("Enter the voltage : ")
                samsung_screen_size = input("Enter the screen size : ")
                samsung_serial = input("Enter the serial number : ")
                product_list.append(samsung_price)
                product_list.append(samsung_weight)
                product_list.append(samsung_voltage)
                product_list.append(samsung_screen_size)
                product_list.append(samsung_serial)


            elif mobile_model == "apple":
                apple_price = float(input("Enter the price : "))
                apple_weight = input("Enter the weight : ")
                apple_voltage = float(input("Enter the voltage : "))
                apple_screen_size = input("Enter the screen size : ")
                apple_standard = input("Enter the standard : ")
                product_list.append(apple_price)
                product_list.append(apple_weight)
                product_list.append(apple_voltage)
                product_list.append(apple_screen_size)
                product_list.append(apple_standard)



        elif elec_type == "laptop":
            laptop_model = input("Is it Asus : ").lower()
            product_list.append(laptop_model)
            print(product_list)
            if laptop_model == "asus":
                asus_price = float(input("Enter the price : "))
                asus_weight = input("Enter the weight : ")
                asus_voltage = input("Enter the voltage : ")
                asus_cpu = input("Enter it's CPU : ")
                asus_ram = input("Enter it's RAM : ")
                asus_make_country = input("Enter it's maker's country : ")
                product_list.append(asus_price)
                product_list.append(asus_weight)
                product_list.append(asus_voltage)
                product_list.append(asus_cpu)
                product_list.append(asus_ram)
                product_list.append(asus_make_country)



        elif elec_type == "monitor":
            monitor_model = input("Is it LG : ").lower()
            product_list.append(monitor_model)
            print(product_list)
            if monitor_model == "lg":
                LG_price = float(input("Enter the price : "))
                LG_weight = input("Enter the weight : ")
                LG_voltage = input("Enter the voltage : ")
                LG_contrast = input("Enter the contrast : ")
                LG_monitor_type = input("Enter the type of monitor : ")
                product_list.append(LG_price)
                product_list.append(LG_weight)
                product_list.append(LG_voltage)
                product_list.append(LG_contrast)
                product_list.append(LG_monitor_type)


    elif elec_unelec == "unelectric":
        elec_type = input("Is it Sofa or Table : ").lower()
        product_list.append(elec_type)
        print(product_list)
        if elec_type == "table" or elec_type == "sofa":
            unelec_usage = input("Enter it's usage : ")
            product_list.append(unelec_usage)
            print(product_list)
            unelec_price = float(input("Enter the price : "))
            product_list.append(unelec_price)
            print(product_list)
            unelec_weight = input("Enter the weight : ")
            product_list.append(unelec_weight)
            print(product_list)

print(product_list)
product_list_2.append(product_list)
for i in product_list_2:
    if i[1] == "electric":
        if i[2] == "mobile":
            mbl = Mobile(i[3], i[4], i[5], i[6], i[7])
            mbl.saver(i[3], "electric", i[6], i[5], i[4], None)
            # print("a")
        elif i[2] == "laptop":
            lp=Laptop(i[3], i[4], i[5], i[6], i[7], i[8])
            lp.saver(i[3], "electric", i[6], i[5], i[4], None)
            # print("b")
        elif i[2] == "monitor":
            mntr = Monitor(i[3], i[4], i[5], i[6], i[7])
            mntr.saver(i[3], "monitor", i[6], i[5], i[4], None)
            # print("c")
    elif i[1] == "unelectric":
        tbl = Table(i[2], i[4], i[5], i[3])
        tbl.saver(i[2], "unelectric", 1, 1, 1, i[3])
        # print("d")
# print(product_list)