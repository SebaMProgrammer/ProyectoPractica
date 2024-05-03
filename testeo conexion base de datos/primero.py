import tkinter as tk
from tkinter import ttk
from database import conectar_base_datos

class PrimeroPage(ttk.Frame):
    def __init__(self, parent, show_home_callback):
        super().__init__(parent)
        
        self.show_home_callback = show_home_callback
        
        self.boton_volver = ttk.Button(self, text="Volver a Home", command=self.volver_a_home)
        self.boton_volver.grid(row=0, column=0, padx=10, pady=10)
        
        self.boton_conectar_db = ttk.Button(self, text="Conectar a Base de Datos", command=self.conectar_bd)
        self.boton_conectar_db.grid(row=1, column=0, padx=10, pady=10)
        
    def conectar_bd(self):
        conexion = conectar_base_datos()
        if conexion:
            self.boton_conectar_db.config(state="disabled")
            # Aquí puedes realizar otras acciones relacionadas con la base de datos
        
    def volver_a_home(self):
        self.show_home_callback()