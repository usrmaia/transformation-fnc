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


form = "-(p#q)" # (-p^-q)
form = get_morgan(form, "p", "q", 3)
print(form)