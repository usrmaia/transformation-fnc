import string

# ...(p>
# ...(-p>
# ...((...)>
# ...(-(...)>
# Retorna subfórmula a esquerda de >
def get_subform_left(A, index):
    open_parenthesis = close_parenthesis = 0
    subform_left = ""
    index_subform = index
    while close_parenthesis >= open_parenthesis:
        index_subform -= 1
        subform_left = A[index_subform] + subform_left
        if A[index_subform] == "(":
            open_parenthesis += 1
        elif A[index_subform] == ")":
            close_parenthesis += 1
    return subform_left[1:]

# >p)...
# >-p)...
# >(...))...
# >-(...))...
# Retorna subfórmula a direita de >
def get_subform_right(A, index):
    open_parenthesis = close_parenthesis = 0
    subform_right = ""
    index_subform = index
    while open_parenthesis >= close_parenthesis:
        index_subform += 1
        subform_right = subform_right + A[index_subform]
        if A[index_subform] == "(":
            open_parenthesis += 1
        elif A[index_subform] == ")":
            close_parenthesis += 1
    return subform_right[:-1]

# Transforma ...((...)>(...))... em ...(-(...)#(...))...
def get_conditional(A, subform_left, subform_right, index):
    A_left = A[:index - len(subform_left)] + "-" + subform_left
    index += 1 
    A_right = A[index:]
    return A_left + "#" + A_right 

# ...(p>q)...
# ...(p>-q)...
# ...(-p>q)...
# ...(-p>-q)...
# ...((p>q)>p)...

def remove_double_negation(A):
    A = A.replace("--", "")
    return A

def redefine(A):
    index = 0
    while index != len(A) - 1:
        index += 1
        implication = A[index]
        if(implication == ">"):
            subform_left = get_subform_left(A, index)
            print("subform_left = " + subform_left)
            subform_right = get_subform_right(A, index)
            print("subform_right = " + subform_right)
            A = get_conditional(A, subform_left, subform_right, index)
            A = remove_double_negation(A)
    return A

# ...(p>q)...
# ...(p>-q)...
# ...(-p>q)...
# ...(-p>-q)...
# ...((p>q)>p)...

form = "...((---p>q)>p)..."
form = redefine(form)
print(form)