# def func(x):
#     return x * (x * (x - 3) + 2) - 6
#
#
# def bisection(a, b, epsilon):
#     if func(a) * func(b) >= 0:
#         return print("Błędne założenie!\n")
#
#     srodek = 0
#     while (b - a) >= epsilon:
#
#         srodek = (a + b) / 2
#
#         if func(srodek) == 0.0:
#             break
#
#         if func(a) * func(srodek) < 0:
#             b = srodek
#         else:
#             a = srodek
#
#     return print("Miejsce zerowe wynosi:" + f"{srodek: .5f}")
#
#
# a = int(input("Podaj zakres przedziałów: \n"))
# b = int(input(""))
#
# epsilon = 0.00001
#
# bisection(a, b, epsilon)


# rozwiązanie rekurencyjne


def func(x):
    return x * (x * (x - 3) + 2) - 6


def bisection(a, b, epsilon):
    if func(a) * func(b) >= 0:
        return print("Błędne założenie!\n")

    srodek = (a + b) / 2

    if b - a <= epsilon:
        return srodek

    if func(a) * func(srodek) < 0:
        return bisection(a, srodek, epsilon)

    return bisection(srodek, b, epsilon)


a = int(input("Podaj zakres przedziałów: \n"))
b = int(input(""))

epsilon = 0.00001

print("Miejsce zerowe wynosi:" + f"{bisection(a, b, epsilon): .5f}")
