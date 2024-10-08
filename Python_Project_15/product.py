import re
import tkinter.messagebox as msg
from validator import *

import mysql.connector


class Product:
    def __init__(self, id, name, brand, quintity, price, person):
        self.id = id
        self.name = name
        self.brand = brand
        self.quintity = quintity
        self.price = price
        self.person = person

    def __str__(self):
        return f'{self.name} {self.brand} {self.quintity} {self.price} {self.person}'

    def name_validator(self):
        if re.match(r"^[a-zA-Z\d\s]{3,30}$", self.name):
            return True
        else:
            return False

    def brand_validator(self):
        if re.match(r"^[a-zA-Z\s\d]{3,30}$", self.brand):
            return True
        else:
            return False

    def save(self):
        if self.name_validator() and self.brand_validator():
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="r@dm@ns@r@1358",
                database="radman"
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO PRODUCT(NAME, BRAND, QUINTITY, PRICE, PERSON) VALUES (%s, %s, %s, %s, %s)",
                           [self.name, self.brand, self.quintity, self.price, self.person])

            connection.commit()
            cursor.close()
            connection.close()
            return True, "saved!"
        else:
            return False, msg.showerror("Error", "Please enter valid name and brand!")

    def edit(self):
        if self.name_validator() and self.brand_validator():
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="r@dm@ns@r@1358",
                database="radman"
            )
            cursor = connection.cursor()
            cursor.execute("UPDATE product SET NAME=%s, BRAND=%s,QUINTITY=%s, PRICE=%s, PERSON=%s WHERE ID=%s",
                           [self.name, self.brand, self.quintity, self.price, self.person, self.id])
            connection.commit()
            cursor.close()
            connection.close()
            return True, "edited!"
        else:
            return False, msg.showerror("Error", "Please enter valid name and brand!")

    def delete(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="r@dm@ns@r@1358",
            database="radman"
        )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM product WHERE ID=%s", [self.id])
        connection.commit()
        cursor.close()
        connection.close()

    def find_all(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="r@dm@ns@r@1358",
            database="radman"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM product")
        product_list = cursor.fetchall()
        product_list_2 = []
        cursor.close()
        connection.close()
        for i in product_list:
            print(i)

    def find_by_id(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="r@dm@ns@r@1358",
            database="radman"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM product WHERE ID=%s", [self.id])
        product_list = cursor.fetchall()
        cursor.close()
        connection.close()
        for i in product_list:
            print(i)

    def find_by_name(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="r@dm@ns@r@1358",
            database="radman"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM product WHERE NAME=%s", [self.name])
        product_list = cursor.fetchall()
        cursor.close()
        connection.close()
        for i in product_list:
            print(i)
