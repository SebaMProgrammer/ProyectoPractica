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
        cur.execute("SELECT * FROM empleados")
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
    
    def inserta_empleado(self,nombre_completo, rut, rol):
        cur = self.cnn.cursor()
        sql='''INSERT INTO countries (nombre_completo, rut, rol) 
        VALUES('{}', '{}', '{}')'''.format(nombre_completo, rut, rol)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_pais(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM countries WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_pais(self,Id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}',
        CurrencyCode='{}' WHERE Id={}'''.format(ISO3, CountryName, Capital, CurrencyCode,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
