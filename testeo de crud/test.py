import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root",
passwd="admin",database="world")
print(cnn)