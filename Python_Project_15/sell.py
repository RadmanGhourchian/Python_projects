import mysql.connector

class Sell:
    def __init__(self, id, person, product, quantity, price):
        self.id = id
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
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='r@dm@ns@r@1358',
            database='radman'
        )
        cursor = connection.cursor()
        cursor.execute("UPDATE radman.product SET QUINTITY= (QUINTITY - %s) WHERE ID=%s", [self.quantity, self.id])
        connection.commit()
        cursor.close()
        connection.close()