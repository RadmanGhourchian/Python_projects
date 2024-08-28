import mysql.connector


def save(name, brand, quintity, price):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="r@dm@ns@r@1358",
        database="test"
    )
    cursor = connection.cursor()
    cursor.execute("INSERT INTO product(NAME, BRAND, QUINTITY, PRICE) VALUES (%s, %s, %s, %s)", (name, brand, quintity, price))

    connection.commit()
    cursor.close()
    connection.close()

def edit(id, name, brand, quintity, price):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="r@dm@ns@r@1358",
        database="test"
    )
    cursor = connection.cursor()
    cursor.execute("UPDATE PRODUCT SET NAME=%S, BRAND=%s, QUINTITY=%s, PRICE=%s WHERE ID=%S",
                   (name, brand, quintity, price))

    connection.commit()
    cursor.close()
    connection.close()

def delete(id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="r@dm@ns@r@1358",
        database="test"
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM PRODUCT WHERE ID=%s", [id])

    connection.commit()
    cursor.close()
    connection.close()

def find_all():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="r@dm@ns@r@1358",
        database="test"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PRODUCT")
    product_list = cursor.fetchall()
    cursor.close()
    connection.close()

def find_by_id(id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="r@dm@ns@r@1358",
        database="test"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PRODUCT WHERE ID=%s", [id])
    lists = cursor.fetchall()
    cursor.close()
    connection.close()

def find_by_name(name):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="r@dm@ns@r@1358",
        database="test"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PRODUCT WHERE NAME=%s", [name])
    lists = cursor.fetchall()
    cursor.close()
    connection.close()