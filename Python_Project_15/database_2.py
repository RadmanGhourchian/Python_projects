import mysql.connector

def find_all():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='r@dm@ns@r@1358',
        database='radman'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM product_2')
    people = cursor.fetchall()
    cursor.close()
    connection.close()
    return people