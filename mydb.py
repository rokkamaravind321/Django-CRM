import mysql.connector

dataBase= mysql.connector.connect(user='root', password='',
                              host='localhost')

cursorObject= dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Database created")
