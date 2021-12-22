from useful import *
from os import system

def remove_implication(formula):
    while ">" in formula:
        operator = formula.find(">")

        print(formula, operator)
        subform_left = get_subform_left(formula, operator)
        subform_right = get_subform_right(formula, operator)
        formula = get_remove_implication(formula, subform_left, subform_right, operator)
    return formula

def get_remove_implication(formula, subform_left, subform_right, operator):
    # ...(A>B)... |-> ...(-A#B)...
    no_modification_right = formula[operator + len(subform_right) + 1:]
    no_modification_left = formula[:operator - len(subform_left)]
    return f"{no_modification_left}-{subform_left}#{subform_right}{no_modification_right}"

def morgan_law(formula):
    while "-(" in formula:
        index = formula.find("-(")
        
        print(formula, index)
        operator = get_operator(formula, index + 1)
        subform_left = get_subform_left(formula, operator)
        subform_right = get_subform_right(formula, operator)
        formula = get_morgan_law(formula, subform_left, subform_right, operator)
    return formula

def get_morgan_law(formula, subform_left, subform_right, operator):
    # ...-(A&B)... |-> ...(-A#-B)...
    # ...-(A#B)... |-> ...(-A&-B)...
    match formula[operator]:
        case "#":
            new_operator = "&"
        case "&":
            new_operator = "#"
    
    no_modification_right = formula[operator + len(subform_right) + 1:]
    no_modification_left = formula[:operator - len(subform_left) - 1 - 1]
    return f"{no_modification_left}(-{subform_left}{new_operator}-{subform_right}{no_modification_right}"

def remove_double_negation(formula):
    # --A |-> A
    formula = formula.replace("--", "")
    return formula

def distributivity(formula):
    index = 0
    while index < len(formula):
        # Existir "#(" ou ")#" é apenas a primeira condição para se aplicar a distributividade
        # A segunda condição é existir "#(A&B)" ou "(A&B)#"
        if "#(" in formula[index:index + 2]: # "#("
            operator_and = get_operator(formula, index + 1)
            if formula[operator_and] == "&": # "#(A&B)"
                print(formula, index, operator_and)
                formula, index = get_distributivity_lr(formula, index, operator_and)
        if ")#" in formula[index:index + 2]: # "(#"
            len_subform_left = len(get_subform_left(formula, index + 1))
            operator_and = get_operator(formula, index + 1 - len_subform_left)
            if formula[operator_and] == "&": # "(A&B)#"
                print(formula, index + 1, operator_and)
                formula, index = get_distributivity_rl(formula, index + 1, operator_and)
        index += 1
    return formula

def get_distributivity_lr(formula, operator_or, operator_and):
    # ...(A#(B&C))... |-> ...((A#B)&(A#C))...
    # Parenteses externo da fórmula
    subform_left = get_subform_left(formula, operator_or)
    no_modification_left = formula[:operator_or - len(subform_left)]
    subform_right = get_subform_right(formula, operator_or)
    no_modification_right = formula[operator_or + len(subform_right) + 1:]

    # Parenteses interno da fórmula
    subform_middle = get_subform_left(formula, operator_and)
    subform_right = get_subform_right(formula, operator_and)

    return f"{no_modification_left}({subform_left}#{subform_middle})&({subform_left}#{subform_right}){no_modification_right}", 0

def get_distributivity_rl(formula, operator_or, operator_and):
    # ...((A&B)#C)... |-> ...((A#C)&(B#C))...
    # Parenteses externo da fórmula
    subform_left = get_subform_left(formula, operator_or)
    no_modification_left = formula[:operator_or - len(subform_left)]
    subform_right = get_subform_right(formula, operator_or)
    no_modification_right = formula[operator_or + len(subform_right) + 1:]

    # Parenteses interno da fórmula    
    subform_left = get_subform_left(formula, operator_and)
    subform_middle = get_subform_right(formula, operator_and)

    return f"{no_modification_left}({subform_left}#{subform_right})&({subform_middle}#{subform_right}){no_modification_right}", 0

if __name__ == "__main__":
    system("cls")
    #system("clear")
    while(True):
        formula = input("Fórmula: ")
        if formula == 'q': break
        print(formula)
        print("Removendo implicações: ")
        A1 = remove_implication(formula)
        print(A1)
        print("Aplicando Lei de Morgan: ")
        A2 = morgan_law(A1)
        print(A2)
        print("Removendo dupla negação: ")
        A3 = remove_double_negation(A2)
        print(A3)
        print("Aplicando distributividade: ")
        B = distributivity(A3)
        print(B)
        system("pause")