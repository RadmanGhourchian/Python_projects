product_list = []
product = input("Enter a product name: ")
while product.lower() != "exit":
    product_list.append(product.lower())
    product = input("Enter a product name: ")

for i in range(len(product_list)):
    a = product_list.index(product_list[i])
    if i > a:
        continue
    else:
        print(product_list[i], "-->", product_list.count(product_list[i]) * "* ")