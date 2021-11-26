import fnc
from tkinter import *
from tkinter import ttk

def ttk_button():
    A = form.get()    
    console_text["text"] = fnc.fnc(A)

root = Tk()
root.title("Transformação em FNC")
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Insira uma fórmula válida para deixa-lá em FNC!").grid(column=0, row=0)
form = Entry(frm, justify="center")
form.grid(column=0, row=1)
ttk.Button(frm, text="Resolver", command=ttk_button).grid(column=0, row=2)
console_text = ttk.Label(frm, text="", justify="center")
console_text.grid(column=0, row=3)
root.mainloop()