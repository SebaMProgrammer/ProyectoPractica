import tkinter as tk
import importlib
from paginaempleados import mostrar_ventana_empleados

class MasterWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto - Página de Inicio")
        self.geometry("400x300")

        self.label = tk.Label(self, text="¡Bienvenido a mi proyecto!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.button_page1 = tk.Button(self, text="Modificar Posicionamientos", command=self.open_page1)
        self.button_page1.pack(pady=10)

        self.button_page2 = tk.Button(self, text="Lista de empleados", command=self.open_page2)
        self.button_page2.pack(pady=10)

    def open_page1(self):
        self.load_page("paginaposicionamiento")

    def open_page2(self):
        mostrar_ventana_empleados()

    def load_page(self, page_name):
        pass

    def show_page(self, page):
        for widget in self.winfo_children():
            widget.pack_forget()
        page.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = MasterWindow()
    root.mainloop()
