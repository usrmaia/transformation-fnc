from os import remove
import string

def get_index(A, index):
    if index >= len(A):
        index = 0
    else:
        index += 1
    return index

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
            input()
            print(A, index)
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
            input()
            print(A, index)
            index_key = get_key(A, index + 1)
            subform_left = get_subform_left(A, index_key)
            subform_right = get_subform_right(A, index_key)
            A = get_morgan_law(A, subform_left, subform_right, index_key)
            #A = remove_double_negation(A)
        index = get_index(A, index)
    return A

# (r#(p^q)) |-> ((r#p)^(r#q))
# ...((...)#((...)^(...)))... |-> ...(((...)#(...))^((...)#(...)))
# Aplica distributividade da esquerda para direita
def get_distributivity_lr(A, index):
    # Principal da fórmula
    first_key = A[index]

    subform_left = get_subform_left(A, index)
    A_left = A[:index - len(subform_left)]
    subform_right = get_subform_right(A, index)
    A_right = A[index + len(subform_right) + 1:]

    # Dentro do parenteses da fórmula
    second_index = get_key(A, index + 1)
    second_key = A[second_index]

    if first_key == "#" and second_key == "^":
        second_subform_left = get_subform_left(A, second_index)
        second_subform_right = get_subform_right(A, second_index)

        return A_left + "(" + subform_left + first_key + second_subform_left + ")" + second_key + "(" + subform_left + first_key + second_subform_right + ")" + A_right, index - len(subform_left)
    return A, index

# ((p^q)#r) |-> ((p#r)^(q#r))
# ...(((...)^(...))#(...))... |-> ...(((...)#(...))^((...)#(...)))
# Aplica distributividade da direita para esquerda
def get_distributivity_rl(A, index):
    # Principal da fórmula
    first_key = A[index]

    subform_left = get_subform_left(A, index)
    A_left = A[:index - len(subform_left)]
    subform_right = get_subform_right(A, index)
    A_right = A[index + len(subform_right) + 1:]

    # Dentro do parenteses da fórmula
    second_index = get_key(A, index - len(subform_left))
    second_key = A[second_index]

    if first_key == "#" and second_key == "^":    
        second_subform_left = get_subform_left(A, second_index)
        second_subform_right = get_subform_right(A, second_index)

        return A_left + "(" + second_subform_left + first_key + subform_right + ")" + second_key + "(" + second_subform_right + first_key + subform_right + ")" + A_right, index - len(subform_left)
    return A, index

# Aplica distributividade em toda a fórmula
def distributivity(A):
    '''
    index = 0
    while "#(" in A or ")#" in A:
        if "#(" in A[index:index + 2]:
            input()
            print(A, index)
            A = get_distributivity_lr(A, index)
        if ")#" in A[index:index + 2]:
            input()
            print(A, index + 1)
            A = get_distributivity_rl(A, index + 1)

        index = get_index(A, index)
    '''
    for index in range(len(A)):
        if "#(" in A[index:index + 2]:
            input()
            print(A, index)
            A, index = get_distributivity_lr(A, index)
        if ")#" in A[index:index + 2]:
            input()
            print(A, index + 1)
            A, index = get_distributivity_rl(A, index + 1)
    return A

# A <-> A1 <-> A2 <-> A3 = B
# Função main
def fnc():
    A = "((p#q)>-(q#r))"
    print(A)
    #A = input("Insira uma fórmula VÁLIDA: ")
    print("Removendo todas as implicações: ")
    A1 = remove_implication(A)
    print(A1)
    print("Aplicado Lei de Morgan para toda a fórmula: ")
    A2 = morgan_law(A1)
    print(A2)
    print("Removendo as dupla negações: ")
    A3 = remove_double_negation(A2)
    print(A3)
    print("Aplicando distributividade: ")
    B = distributivity(A3)
    print(B)
    return(B)

fnc()