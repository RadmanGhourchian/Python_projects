from sell import *
from person import *
from product import *

person = Person("1", "radman", "ghourchian", "1234567890", "radman", 1234)
product = Product("12", "laptop", "samsung", 1, 1400)

sell = Sell(person, product, 3, 1000)


print(product.find_by_id())
