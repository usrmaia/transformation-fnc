from string import ascii_lowercase
from useful import *
from os import system

def verify_semantics(formula):
    try:
        isformula = verify(formula)
        if not isformula:
            print("Não é fórmula proposicional!")
        return isformula
    except:
        print("Não é fórmula proposicional! Possível erro nos parênteses!")
        return False

def verify(formula):
    operator, type = get_operator_type(formula) # operator posição #&>- 
    match type:
        case "Binário": # conectivos #&>
            subform_left = get_subform_left(formula, operator)
            subform_right = get_subform_right(formula, operator)
            sizes = check_sizes(formula, subform_left, subform_right, type)
            return verify(subform_left) and verify(subform_right) and sizes
        case "Unário": # conectivo -
            subform_right = get_subform_right_negation(formula, operator)
            sizes = check_sizes(formula, "", subform_right, type)
            return verify(subform_right) and sizes
        case "Atômico":
            sizes = check_sizes(formula, "", "", type)
            return sizes
        case _:
            return False

def check_sizes(formula, subform_left, subform_right, type):
    """Compara os tamanho considerando o tipo para retornar True/False"""
    formula = len(formula)
    subform_left = len(subform_left)
    subform_right = len(subform_right)

    if type == "Binário":
        return formula == subform_left + subform_right + 3
    elif type == "Unário":
        return formula == subform_right + 1
    elif type == "Atômico":
        return formula == 1

def get_operator_type(formula):
    """Retorna posição do operador principal e tipo da formula"""
    if formula[0] in ascii_lowercase:
        return 0, "Atômico"
    elif formula[0] == "-":
        return 0, "Unário"

    operator = get_operator(formula, 0)
    return operator, "Binário"

if __name__ == "__main__":
    system("cls")
    #system("clear")
    while True:
        formula = input("Fórmula: ")
        if formula == 'q': break
        print(verify_semantics(formula))