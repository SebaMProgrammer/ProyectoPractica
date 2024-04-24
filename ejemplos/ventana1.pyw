import tkinter as tk

class Application(tk.Frame): #frame es clase padre, application clase heredada
    def __init__(self,master=None): #master es el contenedor base
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there =tk.button(self) #crea un botón
        self.hi_there["text"]= "Hello World/n (click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pacl(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                                command=self.master.destroy)
        self.quit.pack(Side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk () #crea la ventana
app = Application(master=root) #establece la ventana "root" como el hijo del master
app.mainloop()