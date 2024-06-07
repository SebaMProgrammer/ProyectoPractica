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

        # Frame izquierdo para la lista de empleados activos
        self.frame_izquierdo = tk.Frame(self, bg="#d3dde3")
        self.frame_izquierdo.place(x=50, y=50, width=500, height=500)

        self.label_empleados = tk.Label(self.frame_izquierdo, text="Empleados Activos", font=("Arial", 12))
        self.label_empleados.pack(pady=10)

        # Treeview para mostrar los empleados activos
        self.tree_empleados = ttk.Treeview(self.frame_izquierdo, columns=("ID", "Nombre", "Rut", "Rol"), show="headings")
        self.tree_empleados.heading("ID", text="ID")
        self.tree_empleados.heading("Nombre", text="Nombre")
        self.tree_empleados.heading("Rut", text="Rut")
        self.tree_empleados.heading("Rol", text="Rol")

        self.tree_empleados.column("ID", width=50)
        self.tree_empleados.column("Nombre", width=150)
        self.tree_empleados.column("Rut", width=100)
        self.tree_empleados.column("Rol", width=100)

        self.tree_empleados.pack(fill="both", expand=True)

        # Llenar la lista de empleados activos
        self.cargar_empleados_activos()

        # Separación entre el frame derecho y el borde de la ventana
        separacion = 20

        # Frame derecho para las mesas de trabajo
        self.frame_derecho = tk.Frame(self, bg="#d3dde3")
        self.frame_derecho.place(x=self.winfo_width() - 500 - separacion, y=50, width=500, height=500)  # Posicionamiento dinámico

        # Crear los contenedores rectangulares para las mesas de trabajo
        self.mesas = []
        for i in range(7):
            mesa_frame = tk.Frame(self.frame_derecho, bg="white", bd=2, relief="solid")
            mesa_frame.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)
            self.mesas.append(mesa_frame)

    def cargar_empleados_activos(self):
        empleados = Empleados()
        datos = empleados.consulta_empleados()
        for row in datos:
            if row[4] == 1:  # Filtrar solo empleados activos (Activo == 1)
                self.tree_empleados.insert("", "end", values=(row[0], row[1], row[2], row[3]))

def mostrar_pagina_posicionamiento():
    app = PaginaPosicionamientos()
    app.mainloop()

if __name__ == "__main__":
    mostrar_pagina_posicionamiento()
