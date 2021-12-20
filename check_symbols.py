from string import ascii_lowercase
from useful_formula import *

def main():
    formula = False
    valid = parse_syntax(formula)
    print(valid)

def parse_syntax(formula):
    # Considere 1 uma sintaxe válida
    formula = check_propositional_symbol(formula)
    formula = check_connective(formula)
    formula = remove_keys(formula)
    formula = confirm_formula(formula)
    return formula

def check_propositional_symbol(formula):
    for letter in ascii_lowercase:
        formula = formula.replace(letter, "1")
    return formula

def check_connective(formula):
    for symbol in ['&', '#', '>', '-', '(', ')']:
        formula = formula.replace(symbol, "1")
    return formula

def remove_keys(formula):
    while "1" in formula:
        formula = formula.replace("1", "")
    return formula

def confirm_formula(formula):
    if len(formula) == 0:
        return True
    return False

if __name__ == "__main__":
    main()