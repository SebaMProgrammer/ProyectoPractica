import tkinter as tk
from tkinter import ttk
from home import HomePage
from primero import PrimeroPage

def main():
    ventana = tk.Tk()
    ventana.title("Aplicación")
    
    def show_db():
        pagina_home.grid_forget()
        pagina_primero.grid()
        
    def show_home():
        pagina_primero.grid_forget()
        pagina_home.grid()
    
    # Crear página "Home"
    pagina_home = HomePage(ventana, show_db)
    pagina_home.grid(row=0, column=0, sticky="nsew")
    
    # Crear página "Primero"
    pagina_primero = PrimeroPage(ventana, show_home)
    
    ventana.mainloop()

if __name__ == "__main__":
    main()