import tkinter as tk
import os

class MasterWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto - Página de Inicio")
        self.geometry("400x300")

        self.label = tk.Label(self, text="¡Bienvenido a mi proyecto!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Abrir Página 1", command=self.open_page1)
        self.button.pack(pady=10)

        self.button2 = tk.Button(self, text="Abrir Página 2", command=self.open_page2)
        self.button2.pack(pady=10)

    def open_page1(self):
        os.system("start pagina1")

    def open_page2(self):
        os.system("start pagina2")

if __name__ == "__main__":
    root = MasterWindow()
    root.mainloop()