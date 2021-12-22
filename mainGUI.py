from os import error
from os import system
from transformation_fnc import *
from verify_semantics import *
from verify_syntax import *
from tkinter import *
from tkinter import ttk

def ttk_button():
    try:
        main()
    except error:
        print(error)

def main():
    formula = form.get()

    system("cls")

    print("Sintaxe: ")
    isformula_syntax = verify_syntax(formula)  
    print(str(isformula_syntax))
    console_text_verify_syntax["text"] = isformula_syntax

    print("Semântica: ")
    isformula_semantics = verify_semantics(formula)
    print(str(isformula_semantics))
    console_text_verify_semantics["text"] = isformula_semantics

    if isformula_syntax and isformula_semantics:

        print("Removendo implicação: ")
        A1 = remove_implication(formula)
        print(A1)
        console_text_remove_implication["text"] = A1

        print("Aplicando Lei de Morgan: ")
        A2 = morgan_law(A1)
        print(A2)
        console_text_morgan_law["text"] = A2

        print("Removendo dupla negação: ")
        A3 = remove_double_negation(A2)
        print(A3)
        console_text_remove_double_negation["text"] = A3

        print("Aplicando distributividade: ")
        A4 = distributivity(A3)
        print(A4)
        console_text_distributivity["text"] = A4

        B = A4

        print(B)
        console_text_return["text"] = B

root = Tk()
root.title("Transformação em FNC")
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Insira uma fórmula:").grid(column=0, row=0)
form = Entry(frm, justify="center")
form.grid(column=0, row=1)
ttk.Button(frm, text="Resolver", command=ttk_button).grid(column=0, row=2)

ttk.Label(frm, text="Verificando sintaxe:").grid(column=0, row=3)
console_text_verify_syntax = ttk.Label(frm, text="", justify="center")
console_text_verify_syntax.grid(column=0, row=4)

ttk.Label(frm, text="Verificando semântica:").grid(column=0, row=5)
console_text_verify_semantics = ttk.Label(frm, text="", justify="center")
console_text_verify_semantics.grid(column=0, row=6)

ttk.Label(frm, text="Removendo implicações:").grid(column=0, row=7)
console_text_remove_implication = ttk.Label(frm, text="", justify="center")
console_text_remove_implication.grid(column=0, row=8)

ttk.Label(frm, text="Aplicando Lei de Morgan:").grid(column=0, row=9)
console_text_morgan_law = ttk.Label(frm, text="", justify="center")
console_text_morgan_law.grid(column=0, row=10)

ttk.Label(frm, text="Removendo dupla negação:").grid(column=0, row=11)
console_text_remove_double_negation = ttk.Label(frm, text="", justify="center")
console_text_remove_double_negation.grid(column=0, row=12)

ttk.Label(frm, text="Aplicando distributividade:").grid(column=0, row=13)
console_text_distributivity = ttk.Label(frm, text="", justify="center")
console_text_distributivity.grid(column=0, row=14)

ttk.Label(frm, text="Resultado:").grid(column=0, row=15)
console_text_return = ttk.Label(frm, text="", justify="center")
console_text_return.grid(column=0, row=16)
root.mainloop()