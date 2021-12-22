def get_subform_left(formula, operator):
    # ...(A>... |-> A
    index = operator
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

def get_subform_right(formula, operator):
    # ...>A)... |-> A
    index = operator
    open_parenthesis = close_parenthesis = 0
    subform_right = ""
    while open_parenthesis >= close_parenthesis:
        index += 1
        subform_right = subform_right + formula[index]

        if formula[index] == "(":
            open_parenthesis += 1
        elif formula[index] == ")":
            close_parenthesis += 1

    return subform_right[:-1]

def get_subform_right_negation(formula, operator):
    # -A |-> A
    return formula[operator + 1:]

def get_operator(formula, operator):
    # ...(AxB)... |-> pos(x)
    index = operator
    open_parenthesis = close_parenthesis = 0
    while index < len(formula):
        if formula[index] == "(":
            open_parenthesis += 1
        elif formula[index] == ")":
            close_parenthesis += 1

        if (formula[index] == "#" or formula[index] == ">" or formula[index] == "&"):
            if open_parenthesis == close_parenthesis + 1:
                return index
        index += 1
    return None