list = []

while (add:=input("Do you want to add products(y) : ").lower() == "y"):
    product_name = input("Product Name: ")
    product_number = int(input("Product Number: "))
    product_price = float(input("Product Price: "))
    proudct_list_dict = {"p_name": product_name, "p_number": product_number, "p_price": product_price}
    list.append(proudct_list_dict)

print("------------------------------------")
list_sum = []
for i in list:
    print(i["p_name"], i["p_number"], i["p_price"],"$" , "==>", i["p_number"] * i["p_price"], "$")
    list_sum.append(i["p_number"] * i["p_price"])

print("------------------------------------")
print("The sum of all the prices is : ", sum(list_sum), "$")