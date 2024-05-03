from tkinter import Tk
from ventana import Ventana

def mostrar_ventana_empleados():
    root = Tk()
    root.wm_title("Crud Python MySQL")
    app = Ventana(root)
    app.mainloop()

if __name__ == "__main__":
    mostrar_ventana_empleados()
