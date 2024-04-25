import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root",
passwd="Ryusei-Go4",database="bdejemplopy")
print(cnn)