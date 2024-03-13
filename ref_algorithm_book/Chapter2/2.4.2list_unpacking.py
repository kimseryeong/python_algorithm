first, *rest = [1, 2, 3, 4, 5]
print(first)
print(rest)

def ex_args(a, b, c):
    return a * b * c
L = [2, 3, 4]
print(ex_args(*L))
print(ex_args(2, *L[1:]))