from tkinter import Tk, Label, Button, Entry, Frame

class FrSuma(Frame):
    def __init__(self,master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def fSuma(self):
        n1 = self.txt1.get()
        n2 = self.txt2.get()
        r = float(n1) + float(n2)
        self.txt3.delete(0,'end')
        self.txt3.insert(0,r)

    def create_widgets(self):
        self.lbl1 = Label(self,text="Primer Numero", bg="yellow")
        self.txt1 = Entry(self, bg="pink")
        self.lbl2 = Label(self,text="Segundo Numero", bg="yellow")
        self.txt2 = Entry(self, bg="pink")
        self.btn1=Button(self,text="sumar", command=self.fSuma)
        self.lbl3 = Label(self,text="Resultado", bg="yellow")
        self.txt3 = Entry(self, bg="cyan")

        self.lbl1.place(x=10,y=10, width=100, height=30)
        self.txt1.place(x=120,y=10, width=100, height=30)
        self.lbl2.place(x=10,y=50, width=100, height=30)
        self.txt2.place(x=120,y=50, width=100, height=30)
        self.btn1.place(x=230,y=50, width=80, height=30)
        self.lbl3.place(x=10,y=120, width=100, height=30)
        self.txt3.place(x=120,y=120, width=1000, height=30)


root = Tk()
app = FrSuma(root)
app.mainloop()