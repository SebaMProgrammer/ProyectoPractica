import tkinter as tk

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
        self.destroy()
        page1 = Page1(self)
        page1.grab_set()

    def open_page2(self):
        self.destroy()
        page2 = Page2(self)
        page2.grab_set()

class Page1(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Proyecto - Página 1")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Esta es la Página 1", font=("Arial", 14))
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Volver a la Página de Inicio", command=self.back_to_home)
        self.button.pack(pady=10)

    def back_to_home(self):
        self.destroy()
        master = MasterWindow()
        master.grab_set()

class Page2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Proyecto - Página 2")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Esta es la Página 2", font=("Arial", 14))
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Volver a la Página de Inicio", command=self.back_to_home)
        self.button.pack(pady=10)

    def back_to_home(self):
        self.destroy()
        master = MasterWindow()
        master.grab_set()

if __name__ == "__main__":
    root = MasterWindow()
    root.mainloop()