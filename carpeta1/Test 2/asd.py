Verás, mi aplicación tiene como contexto un area de trabajo, cuyos empleados son mayormente gente con algún tipo de dificultad sensorial, por lo que se busca crear una aplicación de escritorio para que lo usen los supervisores a cargo.

Esta aplicación estará conectada a una base de datos, y al abrirla te llevara a la pagina principal la cual alberga dos botones, uno para ir a la paginaempleados, en la cual el usuario podrá modificar y añadir filas a la base de datos con los empleados, y el segundo botón lleva a paginaposiciones, en la cual el usuario podrá asignar los empleados disponibles de la base de datos, en los puestos de trabajo que el quiera designar

sin embargo de todo esto, solo tengo la pagina empleados y su base de datos correspondiente lista, asi que quiero que trabajemos con la pagina posiciones, te enviaré el codigo python de mis paginas de la aplicación

principal.py:

import tkinter as tk
from tkinter import ttk
from paginaempleados import mostrar_pagina_empleados
from paginaposicionamiento import mostrar_pagina_posicionamiento

class PaginaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Página Principal")
        self.geometry("1200x600")

        self.label = tk.Label(self, text="¡Bienvenido a la página principal!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.button_page1 = tk.Button(self, text="Ir a la página de empleados", command=self.open_and_close_empleados)
        self.button_page1.pack(pady=10)

        self.button_page2 = tk.Button(self, text="Modificar Posicionamientos", command=self.open_and_close_posicionamientos)
        self.button_page2.pack(pady=10)

    def open_and_close_empleados(self):
        self.destroy()  # Cerrar la ventana actual
        mostrar_pagina_empleados()  # Abrir la página de empleados

    def open_and_close_posicionamientos(self):
        self.destroy()  # Cerrar la ventana actual
        mostrar_pagina_posicionamiento()  # Abrir la página de posicionamiento

if __name__ == "__main__":
    app = PaginaPrincipal()
    app.mainloop()

---------------------------------------------

paginaempleados.py:

import tkinter as tk
from ventana import Ventana

class PaginaEmpleados(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Página de Empleados")
        self.geometry("1200x600")

        self.label = tk.Label(self, text="Página de Empleados", font=("Arial", 14))
        self.label.pack(pady=20)

        # Botón para volver a la página principal
        self.button_back = tk.Button(self, text="Volver al menú principal", command=self.close_and_open_principal)
        self.button_back.pack(pady=10)

        # Mostrar la base de datos en la página
        self.ventana_base_datos = Ventana(self)
        self.ventana_base_datos.pack(fill="both", expand=True)

    def close_and_open_principal(self):
        self.destroy()  # Cerrar la ventana actual
        from principal import PaginaPrincipal  # type: ignore # Importar aquí para evitar la importación circular
        PaginaPrincipal()  # Abrir la página principal

def mostrar_pagina_empleados():
    app = PaginaEmpleados()
    app.mainloop()

if __name__ == "__main__":
    mostrar_pagina_empleados()

-----------------------------------------

ventana.py

from tkinter import *
from tkinter import ttk
from empleadosimp import *
from tkinter import messagebox

class Ventana (Frame):

    empleados = Empleados()

    def __init__(self, master=None):
        super().__init__(master,width=1000, height=500)
        self.master = master
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()
        self.llenaDatos()
        self.habilitarCajas("disabled")
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")
    
    def llenaDatos(self):
        datos = self.empleados.consulta_empleados()
        for row in datos:
            print("Valor de Activo en la base de datos:", row[4])
            activo = "NO" if row[4] == 0 else "SI"  # Cambia 0 a "NO" y 1 a "SI"
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], activo))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    
    def habilitarCajas(self,estado):
        self.txtNombre.configure(state=estado)
        self.txtRut.configure(state=estado)
        self.txtRol.configure(state=estado)
        self.txtActivo.configure(state=estado)
    
    def habilitarBtnOper (self,estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnGuardar (self,estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def limpiarCajas(self):
        self.txtNombre.delete(0,END)
        self.txtRut.delete(0,END)
        self.txtRol.delete(0,END)
        self.txtActivo.delete(0,END)

    def limpiarGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def fNuevo(self):
        self.habilitarCajas("normal")
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()
        self.txtNombre.focus()
        self.id=-1  #para el arreglo de la id ante eliminaciones y demas

    def fModificar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento')
        else:
            self.id = clave
            self.habilitarCajas("normal")
            valores = self.grid.item(selected, 'values')
            self.txtNombre.insert(0, valores[0])
            self.txtRut.insert(0, valores[1])
            self.txtRol.insert(0, valores[2])
            # Corregir cómo se obtiene y muestra el valor de "Activo"
            activo = "SI" if valores[3] == "SI" else "NO"  # Obtener el valor correcto de "Activo"
            self.txtActivo.delete(0, END)
            self.txtActivo.insert(0, activo)
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtNombre.focus()




    def fEliminar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected,'text')

        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento')
        else:
            valores = self.grid.item(selected,'values')
            data= str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "¿Deseas eliminar el registro seleccionado?\n" + data )
            if r == messagebox.YES:
                n = self.empleados.elimina_empleados(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiarGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento')
        pass

    def fGuardar(self):
        if self.id ==-1:
            activo = "1" if self.txtActivo.get().upper() == "SI" else "0"  # Convertir "SI" a 1 y "NO" a 0
            self.empleados.inserta_empleado(self.txtNombre.get(), self.txtRut.get(), self.txtRol.get(), activo)
            messagebox.showinfo("Insertarr", 'Elemento insertado correctamente.')
        else:
            activo = "1" if self.txtActivo.get().upper() == "SI" else "0"  # Convertir "SI" a 1 y "NO" a 0
            self.empleados.modifica_empleados(self.id, self.txtNombre.get(), self.txtRut.get(), self.txtRol.get(), activo)
            messagebox.showinfo("Insertarr", 'Elemento insertado correctamente.')
            self.id= -1
        self.limpiarGrid()
        self.llenaDatos()
        self.limpiarCajas()
        self.habilitarBtnGuardar("disabled")
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")

    def fCancelar(self):
        r = messagebox.askquestion("Cancelar", "¿Esta seguro que desea cancelar la operación actual?")
        if r == messagebox.YES:
            self.habilitarBtnGuardar("disabled")
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg ="#bfdaff")
        frame1.place(x=0,y=0,width=93,height=259)

        self.btnNuevo=Button(frame1, text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80, height=30)

        self.btnModificar=Button(frame1, text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)

        self.btnEliminar=Button(frame1, text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)
    
        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=95, y=0, width=150, height=259)

        lbl1 = Label(frame2, text= "Nombre_completo: ")
        lbl1.place(x=3,y=5)
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=3,y=25,width=100, height=20)  

        lbl2 = Label(frame2, text= "Rut: ")
        lbl2.place(x=3,y=55)
        self.txtRut=Entry(frame2)
        self.txtRut.place(x=3,y=75,width=100, height=20)  

        lbl3 = Label(frame2, text= "Rol: ")
        lbl3.place(x=3,y=105)
        self.txtRol=Entry(frame2)
        self.txtRol.place(x=3,y=125,width=100, height=20)

        lbl4 = Label(frame2, text= "Activo: ")
        lbl4.place(x=3,y=155)
        self.txtActivo=Entry(frame2)
        self.txtActivo.place(x=3,y=175,width=100, height=20)    

        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10,y=210,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=210,width=60, height=30)        
        
        frame3 = Frame(self, bg="yellow")
        frame3.place(x=247,y=0,width=525,height=259)

        self.grid =ttk.Treeview(frame3, columns=("col1","col2","col3","col4"))

        self.grid.column("#0",width=60)
        self.grid.column("col1",width=180, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)



        self.grid.heading("#0",text="Id")
        self.grid.heading("col1",text="Nombre Completo", anchor=CENTER)
        self.grid.heading("col2",text="Rut", anchor=CENTER)
        self.grid.heading("col3",text="Rol", anchor=CENTER)
        self.grid.heading("col4",text="Activo", anchor=CENTER)
    

        self.grid.pack(side=LEFT, fill = Y)

        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'

------------------------------------------

empleadosimp:

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
        cur.execute("SELECT ID, Nombre_completo, Rut, Rol, Activo FROM empleados")
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

    def modifica_empleados(self, Id, nombre_completo, Rut, Rol, Activo):
        cur = self.cnn.cursor()
        sql = '''UPDATE empleados SET Nombre_completo='{}', Rut='{}', Rol='{}', Activo='{}' 
                WHERE Id={}'''.format(nombre_completo, Rut, Rol, Activo, Id)  # Agregado {} para Activo
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

--------------------------------------------------------------

# paginaposicionamiento.py

import tkinter as tk
from tkinter import ttk
from empleadosimp import Empleados

class PaginaPosicionamientos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Página de Posicionamientos")
        self.geometry("1200x600")

        self.label = tk.Label(self, text="Página de Posicionamientos", font=("Arial", 14))
        self.label.pack(pady=20)

        # Frame para la lista de empleados activos
        self.frame_izquierdo = tk.Frame(self, bg="#d3dde3")
        self.frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.label_empleados = tk.Label(self.frame_izquierdo, text="Empleados Activos", font=("Arial", 12))
        self.label_empleados.pack(pady=10)

        # Treeview para mostrar los empleados activos
        self.tree_empleados = ttk.Treeview(self.frame_izquierdo, columns=("ID", "Nombre", "Rut", "Rol"), show="headings")
        self.tree_empleados.heading("ID", text="ID")
        self.tree_empleados.heading("Nombre", text="Nombre")
        self.tree_empleados.heading("Rut", text="Rut")
        self.tree_empleados.heading("Rol", text="Rol")

        self.tree_empleados.column("ID", width=10)
        self.tree_empleados.column("Nombre", width=70)
        self.tree_empleados.column("Rut", width=50)
        self.tree_empleados.column("Rol", width=70)

        self.tree_empleados.pack(fill="both", expand=True)

        # Llenar la lista de empleados activos
        self.cargar_empleados_activos()

        # Canvas para las mesas de trabajo
        self.frame_derecho = tk.Frame(self, bg="#ffffff")
        self.frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(self.frame_derecho, bg="#ffffff")
        self.canvas.pack(fill="both", expand=True)

        self.dibujar_mesas()

        self.bind("<Configure>", self.redimensionar)

    def cargar_empleados_activos(self):
        empleados = Empleados()
        datos = empleados.consulta_empleados()
        for row in datos:
            if row[4] == 1:  # Filtrar solo empleados activos (Activo == 1)
                self.tree_empleados.insert("", "end", values=(row[0], row[1], row[2], row[3]))

    def dibujar_mesas(self):
        self.canvas.delete("all")  # Limpiar el canvas antes de redibujar
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        rect_height = height // 7 - 10  # Espacio vertical para cada mesa

        for i in range(7):
            x0 = 50
            y0 = 10 + i * (rect_height + 10)
            x1 = width - 50
            y1 = y0 + rect_height
            self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="#d3d3d3")
            self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=f"Mesa {i+1}", font=("Arial", 12))

    def redimensionar(self, event):
        self.dibujar_mesas()

def mostrar_pagina_posicionamiento():
    app = PaginaPosicionamientos()
    app.mainloop()

if __name__ == "__main__":
    mostrar_pagina_posicionamiento()
