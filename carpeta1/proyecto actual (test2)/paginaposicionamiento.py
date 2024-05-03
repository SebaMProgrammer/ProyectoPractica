import tkinter as tk

def mostrar_mensaje():
    mensaje = tk.Label(root, text="¡Bienvenido!", font=("Arial", 14))
    mensaje.pack(pady=20)

root = tk.Tk()
root.title("Página 2")

boton = tk.Button(root, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack(pady=10)

root.mainloop()