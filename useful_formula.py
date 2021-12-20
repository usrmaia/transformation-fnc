def get_subform_left(formula, index):
    """Retorna subfórmula a esquerda do conectivo"""
    open_parenthesis = close_parenthesis = 0
    subform_left = ""
    while close_parenthesis >= open_parenthesis:
        index -= 1
        subform_left = formula[index] + subform_left
        
        if formula[index] == "(":
            open_parenthesis += 1
        elif formula[index] == ")":
            close_parenthesis += 1
        
    return subform_left[1:]

# >p)... |-> p
# >-p)... |-> -p
# >(...))... |-> (...)
# >-(...))... |-> -(...)
def get_subform_right(A, index):
    """Retorna subfórmula a direita de >"""
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
def get_key(A, index):
    """Retorna operando principal da formula"""
    open_parenthesis = close_parenthesis = 0
    while index < len(A):
        if A[index] == "(":
            open_parenthesis += 1
        elif A[index] == ")":
            close_parenthesis += 1

        if (A[index] == "^" or A[index] == "#" or A[index] == ">"):
            if open_parenthesis == close_parenthesis + 1:
                return index, A[index]
        index += 1
    return None

def get_index(A, index):
    """Retorna valor de index relativo ao tamanho da fórmula"""
    if index >= len(A):
        index = 0
    else:
        index += 1
    return index