import mysql.connector

class Empleados:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="Ryusei-Go4", database="empleados")

    def __str__(self):
        datos=self.consulta_empleados()
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
    
    def consulta_empleados(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT ID, Nombre_completo, Rut, Rol, CASE WHEN Activo = 0 THEN 'NO' ELSE 'SI' END AS Activo FROM empleados")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_empleados(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM empleados WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_empleado(self,nombre_completo, rut, rol, activo):
        cur = self.cnn.cursor()
        sql='''INSERT INTO empleados (nombre_completo, rut, rol, activo) 
        VALUES('{}', '{}','{}','{}')'''.format(nombre_completo, rut, rol, activo)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_empleados(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM empleados WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_empleados(self,Id, nombre_completo, Rut, Rol, Activo):
        cur = self.cnn.cursor()
        sql='''UPDATE empleados SET Nombre_completo='{}', Rut='{}', Rol='{}', Activo='{}' 
        WHERE Id={}'''.format(nombre_completo, Rut, Rol,Id, Activo)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
