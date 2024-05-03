import mysql.connector

def conectar_base_datos():
    try:
        conexion = mysql.connector.connect(
            host="localhost", user="root",
            password="Ryusei-Go4",database="empleados"
        )
        return conexion
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)

def agregar_dato(conexion, dato):
    # Lógica para agregar dato a la base de datos
    pass

def eliminar_dato(conexion, id):
    # Lógica para eliminar dato de la base de datos
    pass

def editar_dato(conexion, id, nuevo_valor):
    # Lógica para editar dato en la base de datos
    pass

def obtener_datos(conexion):
    # Lógica para obtener datos de la base de datos
    pass