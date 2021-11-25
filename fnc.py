from os import remove
import string

# ...(p> |-> p
# ...(-p> |-> -p
# ...((...)> |-> (...)
# ...(-(...)> |-> -(...)
# Retorna subfórmula a esquerda de >
def get_subform_left(A, index):
    open_parenthesis = close_parenthesis = 0
    index_subform = index
    subform_left = ""
    while close_parenthesis >= open_parenthesis:
        index_subform -= 1
        subform_left = A[index_subform] + subform_left
        if A[index_subform] == "(":
            open_parenthesis += 1
        elif A[index_subform] == ")":
            close_parenthesis += 1
    return subform_left[1:]

# >p)... |-> p
# >-p)... |-> -p
# >(...))... |-> (...)
# >-(...))... |-> -(...)
# Retorna subfórmula a direita de >
def get_subform_right(A, index):
    open_parenthesis = close_parenthesis = 0
    index_subform = index
    subform_right = ""
    while open_parenthesis >= close_parenthesis:
        index_subform += 1
        subform_right = subform_right + A[index_subform]
        if A[index_subform] == "(":
            open_parenthesis += 1
        elif A[index_subform] == ")":
            close_parenthesis += 1
    return subform_right[:-1]

# ...(p>q)
# ...(p>-q)...
# ...(-p>q)...
# ...(-p>-q)...
# ...((p>q)>p)...
# Transforma ...((...)>(...))... em ...(-(...)#(...))...
def get_conditional(A, subform_left, subform_right, index):
    A_left = A[:index - len(subform_left)] + "-" + subform_left
    index += 1 
    A_right = A[index:]
    return A_left + "#" + A_right 

def remove_double_negation(A):
    A = A.replace("--", "")
    return A

# ...(p>q)...
# ...(p>-q)...
# ...(-p>q)...
# ...(-p>-q)...
# ...((p>q)>p)...
# Remove todas as > da fórmula
def redefine(A):
    index = 0
    while index != len(A) - 1:
        index += 1
        #implication = A[index]
        if(A[index] == ">"):
            subform_left = get_subform_left(A, index)
            print("subform_left = " + subform_left)
            subform_right = get_subform_right(A, index)
            print("subform_right = " + subform_right)
            A = get_conditional(A, subform_left, subform_right, index)
            A = remove_double_negation(A)
    return A

def get_key(A, index):
    open_parenthesis = close_parenthesis = 0
    while index < len(A) - 1:
        if A[index] == "(":
            open_parenthesis += 1
        elif A[index] == ")":
            close_parenthesis += 1

        if (A[index] == "^" or A[index] == "#"):
            if open_parenthesis == close_parenthesis + 1:
                return index
        index += 1
    return None

def get_morgan(A, subform_left, subform_right, index):
    if A[index] == "#":
        A = A[:index] + "^" + A[index + 1:]
    elif A[index] == "^":
        A = A[:index] + "#" + A[index + 1:]

    A = A[:index - len(subform_left) - 2] + A[index - len(subform_left) - 1:]

    index -= 1

    A_right = "-" + A[index + 1:]
    A_left = A[:index - len(subform_left)] + "-" + subform_left
    return A_left + A[index] + A_right 

# ...-((...)^(...))... |-> ...(-(...)#-(...))...
# -(p^q) |-> (-p#-q)
# -(p#q) |-> (-p^-q)
def morgan_law(A):
    index = 0
    while "-(" in A:
        if "-(" in A[index:index + 2]:
            index_key = get_key(A, index + 1)
            subform_left = get_subform_left(A, index_key)
            subform_right = get_subform_right(A, index_key)
            A = get_morgan(A, subform_left, subform_right, index_key)
            A = remove_double_negation(A)
        index += 1
    return A

A = "...-(--(p#q)^-(p^q))..."
'''
index_key = get_key(A, 3 + 1)
subform_left = get_subform_left(A, 11)
subform_right = get_subform_right(A, 11)
A = get_morgan(A, subform_left, subform_right, 11)
A = remove_double_negation(A)
'''
A = morgan_law(A)
print(A)