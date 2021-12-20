from string import ascii_lowercase
from useful_formula import *

formula = "(a>c>b)"
index = 2
formula = get_subform_right(formula, index)
#formula = formula[:index] + "1" + formula[index + 1:]
if 76:
    print("Teste")
print(formula)