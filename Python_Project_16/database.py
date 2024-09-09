import mysql.connector

class Database:
    def saver(self, name, electric, voltage, weight, price, usage):
        if electric == "electric":
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='r@dm@ns@r@1358',
                database='radman'
            )
            cursor = connection.cursor()
            cursor.execute('INSERT INTO PRODUCTS_ELECTRIC(NAME, ELECTRIC, VOLTAGE, WEIGHT, PRICE) VALUES(%s, %s, %s, %s, %s)', [name, electric, voltage, weight, price])
            connection.commit()
            cursor.close()
            connection.close()
        elif electric == "unelectric":
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='r@dm@ns@r@1358',
                database='radman'
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO products_unelectric (NAME, ELECTRIC, USEAGE) VALUES (%s, %s, %s)", [name, electric, usage])
            connection.commit()
            cursor.close()
            connection.close()

    def edit(self, id, name, electric, voltage, usage):
        if electric == "electric":
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='r@dm@ns@r@1358',
                database='radman'
            )
            cursor = connection.cursor()
            cursor.execute("UPDATE PRODUCTS_ELECTRIC SET NAME=%s, ELECTRIC=%s, VOLTAGE=%s WHERE ID=%s", [name, electric, voltage, id])
            connection.commit()
            cursor.close()
            connection.close()
        elif electric == "unelectric":
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='r@dm@ns@r@1358',
                database='radman'
            )
            cursor = connection.cursor()
            cursor.execute("UPDATE PRODUCTS_UNELECTRIC SET NAME=%S, ELECTRIC=%s, USAGE=%s WHERE ID=%s", [name, electric, usage, id])
            connection.commit()
            cursor.close()
            connection.close()
    def delete(self, id, electric):
        if electric == "electric":
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='r@dm@ns@r@1358',
                database='radman'
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM PRODUCTS_ELECTRIC WHERE ID=%s", [id])
            connection.commit()
            cursor.close()
            connection.close()
        elif electric == "unelectric":
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='r@dm@ns@r@1358',
                database='radman'
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM PRODUCTS_UNELECTRIC WHERE ID=%s", [id])
            connection.commit()
            cursor.close()
            connection.close()

