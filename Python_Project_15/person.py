import mysql.connector


class Person():
    def __init__(self, id, name, family, national_id, username, password):
        self.id = id
        self.name = name
        self.family = family
        self.national_id = national_id
        self.username = username
        self.password = password

    def __str__(self):
        return f'{self.id} {self.name} {self.family} {self.national_id} {self.username} {self.password}'

    def to_tuple(self):
        return (self.id, self.name, self.family, self.national_id, self.username, self.password)

    def save(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='r@dm@ns@r@1358',
            database='radman'
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO PRODUCT_2 (name, family, national_id, username, password) VALUES (%s, %s, %s, %s, %s)",
                       [self.name, self.family, self.national_id, self.username, self.password])
        connection.commit()
        cursor.close()
        connection.close()
    def edit(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='r@dm@ns@r@1358',
            database='radman'
        )
        cursor = connection.cursor()
        cursor.execute("UPDATE product_2 SET NAME=%s, FAMILY=%s,NATIONAL_ID=%s, USERNAME=%s, PASSWORD=%s WHERE ID=%s",
                       [self.name, self.family, self.national_id, self.username, self.password, self.id])
        connection.commit()
        cursor.close()
        connection.close()
    def delete(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='r@dm@ns@r@1358',
            database='radman'
        )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM product_2 WHERE ID=%s", [self.id])
        connection.commit()
        cursor.close()
        connection.close()
