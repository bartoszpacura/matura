from math import fabs


def sq(num):
    a = 1
    eps = 0.000001
    p = num
    b = p
    while fabs(a - b) >= eps:
        a = (a + b) / 2
        print("a: " + str(a))
        b = p / a
        print("b: " + str(b))

    return round(a, 6)


number = float(input("Wpisz liczbę, z której chcesz wyznaczyć pierwiastek kwadratowy?: "))

print("Wyznaczony pierwiastek: " + str(sq(number)))
