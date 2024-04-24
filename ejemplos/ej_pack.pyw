from tkinter import Tk, Label, Button, Entry

vent = Tk()
vent.title("Ejemplo de place")
vent.geometry("400x200")

def fnSuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) + float(n2)
    txt3.insert(0,r)



lbl1 = Label(vent,text="Primer Numero", bg="yellow")
txt1 = Entry(vent, bg="pink")
lbl2 = Label(vent,text="Segundo Numero", bg="yellow")
txt2 = Entry(vent, bg="pink")
btn1=Button(vent,text="sumar", command=fnSuma)
lbl3 = Label(vent,text="Resultado", bg="yellow")
txt3 = Entry(vent, bg="pink")

lbl1.pack(pady=6)
txt1.pack(pady=6)
lbl2.pack(pady=6)
txt2.pack(pady=6)
btn1.pack(pady=6)
txt3.pack(pady=6)
lbl3.pack(pady=6)
vent.mainloop()