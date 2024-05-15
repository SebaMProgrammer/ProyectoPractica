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