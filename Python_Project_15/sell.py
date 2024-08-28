class Sell:
    def __init__(self, person, product, quantity, price):
        self.person = person
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

    def tax(self):
        return Sell.total(self) * 0.09

    def pure_amount(self):
        return Sell.total(self) - Sell.tax(self)

    def sell(self):
        pass