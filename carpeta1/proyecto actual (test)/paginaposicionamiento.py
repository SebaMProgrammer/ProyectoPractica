import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root",
passwd="Ryusei-Go4",database="empleados")

cur = cnn.cursor()
cur.execute("SELECT * FROM empleados")
datos = cur.fetchall()

for fila in datos:
    print(fila)

print(cnn)