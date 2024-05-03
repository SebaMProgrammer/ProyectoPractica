import tkinter as tk
from tkinter import ttk

class HomePage(ttk.Frame):
    def __init__(self, parent, show_db_callback):
        super().__init__(parent)
        
        self.boton_primero = ttk.Button(self, text="Primero", command=show_db_callback)
        self.boton_primero.grid(row=0, column=0, padx=10, pady=10)
        self.boton_segundo = ttk.Button(self, text="Segundo")
        self.boton_segundo.grid(row=1, column=0, padx=10, pady=10)
        
    def conectar_bd(self):
        # Lógica para conectar a la base de datos
        pass