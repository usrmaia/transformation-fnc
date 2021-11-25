from os import remove
import string

# ...(p> |-> p
# ...(-p> |-> -p
# ...((...)> |-> (...)
# ...(-(...)> |-> -(...)
# Retorna subfórmula a esquerda de >
def get_subform_left(A, index):
    open_parenthesis = close_parenthesis = 0
    subform_left = ""
    while close_parenthesis >= open_parenthesis:
        index -= 1
        subform_left = A[index] + subform_left

        if A[index] == "(":
            open_parenthesis += 1
        elif A[index] == ")":
            close_parenthesis += 1
    return subform_left[1:]

# >p)... |-> p
# >-p)... |-> -p
# >(...))... |-> (...)
# >-(...))... |-> -(...)
# Retorna subfórmula a direita de >
def get_subform_right(A, index):
    open_parenthesis = close_parenthesis = 0
    subform_right = ""
    while open_parenthesis >= close_parenthesis:
        index += 1
        subform_right = subform_right + A[index]

        if A[index] == "(":
            open_parenthesis += 1
        elif A[index] == ")":
            close_parenthesis += 1
    return subform_right[:-1]

# ...-(-(p^q)#(p>q))... |-> pos(#)
# ...((...)x(...))... |-> pos(x)
# Retorna operando principal da formula
def get_key(A, index):
    open_parenthesis = close_parenthesis = 0
    while index < len(A):
        if A[index] == "(":
            open_parenthesis += 1
        elif A[index] == ")":
            close_parenthesis += 1

        if (A[index] == "^" or A[index] == "#" or A[index] == ">"):
            if open_parenthesis == close_parenthesis + 1:
                return index
        index += 1
    return None

# ...(p>q)
# ...(p>-q)...
# ...(-p>q)...
# ...(-p>-q)...
# ...((p>q)>p)...
# ...((...)>(...))... |-> ...(-(...)#(...))...
def get_remove_implication(A, subform_left, subform_right, index):
    A_right = A[index + 1:]
    A_left = A[:index - len(subform_left)]
    return A_left + "-" + subform_left + "#" + A_right 

# ...(--(...)>--(...))... |-> ...((...)>(...))...
# Remove dupla negação
def remove_double_negation(A):
    A = A.replace("--", "")
    return A

# ...(p>q)...
# ...(p>-q)...
# ...(-p>q)...
# ...(-p>-q)...
# ...((p>q)>p)...
# (((...>...)>(...>...))>(...>...)) |-> (-(-(-...#...)#(-...#...))#(-...#...))
# Remove todas as > da fórmula
def remove_implication(A):
    index = 0
    while ">" in A:
        index += 1
        if(A[index] == ">"):
            subform_left = get_subform_left(A, index)
            #print("subform_left = " + subform_left)
            subform_right = get_subform_right(A, index)
            #print("subform_right = " + subform_right)
            A = get_remove_implication(A, subform_left, subform_right, index)
            index -= 1
            #A = remove_double_negation(A)
    return A

# -(p^q) |-> (-p#-q)
# -(p#q) |-> (-p^-q)
# -((...)#(...)) |-> (-(...)^-(...))
# -((...)^(...)) |-> (-(...)#-(...))
# Aplica lei de Morgan
def get_morgan_law(A, subform_left, subform_right, index):
    if A[index] == "#":
        key = "^"
    elif A[index] == "^":
        key = "#"
    
    A_right = A[index + 1:]
    A_left = A[:index - len(subform_left) - 1 - 1]
    return A_left + "(" + "-" + subform_left + key + "-" + A_right

# -(p^q) |-> (-p#-q)
# -(p#q) |-> (-p^-q)
# -((...#...)#(...#...)) |-> ((-...^-...)^(-...^-...))
# Aplica Morgan a toda a fórmula
def morgan_law(A):
    index = 0
    while "-(" in A:
        if "-(" in A[index:index + 2]:
            index_key = get_key(A, index + 1)
            subform_left = get_subform_left(A, index_key)
            subform_right = get_subform_right(A, index_key)
            A = get_morgan_law(A, subform_left, subform_right, index_key)
            A = remove_double_negation(A)
        index += 1
    return A

def fnc(A):
    A1 = remove_implication(A)
    A2 = morgan_law(A1)
    A3 = remove_double_negation(A2)
    # Último passo
    return(A3)

print(fnc(input()))