from transformation_fnc import *
from verify_semantics import *
from verify_syntax import *
from tkinter import *
from tkinter import ttk

def ttk_button():
    try:
        A = form.get()    
        console_text_return["text"] = fnc(A)

        A1 = remove_implication(A)
        console_text_remove_implication["text"] = A1

        A2 = morgan_law(A1)
        console_text_morgan_law["text"] = A2

        A3 = remove_double_negation(A2)
        console_text_remove_double_negation["text"] = A3

        B = distributivity(A3)
        console_text_distributivity["text"] = B

        console_text_return2["text"] = fnc(A)
    except:
        print("INSIRA UMA FÓRMULA VÁLIDA!!!")

root = Tk()
root.title("Transformação em FNC")
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Insira uma fórmula válida para deixa-lá em FNC!").grid(column=0, row=0)
form = Entry(frm, justify="center")
form.grid(column=0, row=1)
ttk.Button(frm, text="Resolver", command=ttk_button).grid(column=0, row=2)
# Retorno/Resposta
console_text_return = ttk.Label(frm, text="", justify="center")
console_text_return.grid(column=0, row=3)
space = ttk.Label(frm, text="", justify="center").grid(column=0, row=4)
# Removendo implicações
ttk.Label(frm, text="Removendo todas as implicações:").grid(column=0, row=5)
console_text_remove_implication = ttk.Label(frm, text="", justify="center")
console_text_remove_implication.grid(column=0, row=6)
# Aplicando Morgan
ttk.Label(frm, text="Aplicando Lei de Morgan:").grid(column=0, row=7)
console_text_morgan_law = ttk.Label(frm, text="", justify="center")
console_text_morgan_law.grid(column=0, row=8)
# Removendo duplanegação
ttk.Label(frm, text="Removendo dupla negação:").grid(column=0, row=9)
console_text_remove_double_negation = ttk.Label(frm, text="", justify="center")
console_text_remove_double_negation.grid(column=0, row=10)
# Aplicando distributividade
ttk.Label(frm, text="Aplicando distributividade:").grid(column=0, row=11)
console_text_distributivity = ttk.Label(frm, text="", justify="center")
console_text_distributivity.grid(column=0, row=12)
# Retorno
ttk.Label(frm, text="Resultado:").grid(column=0, row=13)
console_text_return2 = ttk.Label(frm, text="", justify="center")
console_text_return2.grid(column=0, row=14)
root.mainloop()