from tkinter import *
from tkinter import ttk

from empleadosimp import *

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
            activo = "NO" if row[4] == 0 else "SI"  # Cambia 0 a "NO" y 1 a "SI"
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], activo))
    
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

    def fModificar(self):
        pass

    def fEliminar(self):
        pass

    def fGuardar(self):
        self.empleados.inserta_empleado(self.txtNombre.get(), self.txtRut.get(), self.txtRol.get(), self.txtActivo.get())
        self.limpiarGrid()
        self.llenaDatos()
        self.habilitarBtnGuardar("disabled")
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")


    def fCancelar(self):
        pass

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
        self.txtNombre.place(x=3,y=25,width=50, height=20)  

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


        self.grid =ttk.Treeview(self, columns=("col1","col2","col3","col4"))

        self.grid.column("#0",width=50)
        self.grid.column("col1",width=200, anchor=CENTER)
        self.grid.column("col2",width=120, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)



        self.grid.heading("#0",text="Id")
        self.grid.heading("col1",text="Nombre Completo", anchor=CENTER)
        self.grid.heading("col2",text="Rut", anchor=CENTER)
        self.grid.heading("col3",text="Rol", anchor=CENTER)
        self.grid.heading("col4",text="Activo", anchor=CENTER)
    

        self.grid.place(x=247,y=0,width=900,height=259)