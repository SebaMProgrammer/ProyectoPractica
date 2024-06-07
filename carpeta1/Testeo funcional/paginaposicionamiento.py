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

        self.tree_empleados.column("ID", width=5)
        self.tree_empleados.column("Nombre", width=100)
        self.tree_empleados.column("Rut", width=50)
        self.tree_empleados.column("Rol", width=100)

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
