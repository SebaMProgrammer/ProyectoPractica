import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root",
passwd="Ryusei-Go4",database="world")

cur = cnn.cursor()
cur.execute("SELECT * FROM city WHERE CountryCode = 'AFG' s")
datos = cur.fetchall()

for fila in datos:
    print(fila)

print(cnn)