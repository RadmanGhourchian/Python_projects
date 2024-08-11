price_list = []

def get_inf():
    inf = {
        "name": input("Enter your name of the product : "),
        "count": float(input("Enter the count of the product : ")),
        "price": float(input("Enter the price of the product : "))
    }
    return inf


def thousand_dollar(price_list):
    total_price = 0
    for i in price_list:
        total_price = total_price + (i["price"] * i["count"])

    return total_price


def printer(price_list):
    for i in price_list:
        print("The name of your product is : ", i["name"])
        print("The price of your product is : ", i["price"])
        print("The count of your product is : ", i["count"])
        print("The price of all of them is : ", i["price"] * i["count"])
        print("------------------------------------------------------")