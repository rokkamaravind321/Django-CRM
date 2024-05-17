import mysql.connector

dataBase= mysql.connector.connect(user='root', password='password',
                              host='localhost')

cursorObject= dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Database created")