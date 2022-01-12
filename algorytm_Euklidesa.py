# iteration non-optimized

a = int(input(""))
b = int(input(""))

while a != b:
    if a > b:
        a = a - b
    elif a < b:
        b = b - a
print(a)

# iteration optimized

# a = int(input(""))
# b = int(input(""))
# m = 1
#
# while b != 0:
#
#     m = b
#     b = a % b
#     a = m
#
# print(a)


# nad rozwiązaniem rekurencyjnym muszę się jeszcze zastanowić

# recursion non-optimized

# a = int(input(""))
# b = int(input(""))
#
# def recur(n, m):
#     if
#         return
#     else:
#         return recur()
#
# ???


# recursion optimized

# a = int(input(""))
# b = int(input(""))
#
#
# def recur(n_1, n_2):
#
#
# print(recur(a, b))
#
# ???
