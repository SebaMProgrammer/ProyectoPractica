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
        from principal import PaginaPrincipal  # Importar aquí para evitar la importación circular
        PaginaPrincipal()  # Abrir la página principal

def mostrar_pagina_empleados():
    app = PaginaEmpleados()
    app.mainloop()

if __name__ == "__main__":
    mostrar_pagina_empleados()