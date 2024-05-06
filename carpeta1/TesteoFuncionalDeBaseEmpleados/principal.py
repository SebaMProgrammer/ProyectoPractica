import tkinter as tk
from tkinter import ttk
from paginaempleados import mostrar_pagina_empleados
from paginaposicionamiento import mostrar_pagina_posicionamiento

class PaginaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Página Principal")
        self.geometry("400x300")

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