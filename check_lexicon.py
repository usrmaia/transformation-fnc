from string import ascii_lowercase
from useful_formula import *

letters = ascii_lowercase + "1"
connectives = ">#&"

def main():
    formula = "(c>a>b)"
    #print(formula[5])
    formula2 = verify2(formula)

def verify(formula, index):
    if len(formula) == 1:
        if letters_in_formula(formula):
            formula = "1"
            return formula
        return False
    elif "(" in formula[index]:
        formula = verify(formula, index + 1)
        if formula[index + 1] == "1":
            if formula[index + 2] == ")":
                formula = formula.replace("(1)", "1")
                formula = verify(formula, index)
    elif "-" in formula[index]:
        formula = verify(formula, index + 1)
        if letters_in_formula(formula[index + 1]):
            formula = formula[:index] + "1" + formula[index + 2:]
    elif letters_in_formula(formula[index]):
        if connectives_in_formula(formula[index + 1]):
            formula = verify(formula, index + 2)
            if letters_in_formula(formula[index + 2]):
                formula = formula[:index] + "1" + formula[index + 3:]
    return formula
'''
def verify2(formula):
    for index in formula:
        if connectives_in_formula(formula[index]):
            subform_left = get_subform_left(formula, index)
            # colocar na formula_de_retorno
            subform_right = get_subform_right(formula, index)
            # chamar recursivamente
        elif unary_connective(formula[index]):
            subform_right = get_subform_right(formula, index
'''

def verify2(formula):
    index, type = get_key(formula)
    if type == "Binário":
        subform_left = get_subform_left(formula, index)
        subform_right = get_subform_right(formula, index)
        verify2(subform_left)
        verify2(subform_right)
    elif type == "Unário":
        subform_right = get_subform_right(formula, index)
        verify2(subform_right)

def letters_in_formula(formula):
    for letter in letters:
        if letter in formula:
            return True
    return False

def connectives_in_formula(formula):
    for connective in connectives:
        if connective in formula:
            return True
    return False

def unary_connective(formula):
    if "-" in formula:
        return True
    return False

def replace(formula, index):
    return formula[:index] + "1" + formula[index + 1:]

def get_key(A):
    """Retorna operando principal da formula"""
    open_parenthesis = close_parenthesis = index = 0
    while index < len(A):
        if A[index] == "(":
            open_parenthesis += 1
        elif A[index] == ")":
            close_parenthesis += 1

        if (A[index] == "^" or A[index] == "#" or A[index] == ">"):
            if open_parenthesis == close_parenthesis + 1:
                return index, "Binário"
        elif A[index] == "-":
            return index, "Unário"
        index += 1
    return None



if __name__ == "__main__":
    main()