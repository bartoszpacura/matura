def funkcja(x):
    return x * x + x + 2

def pole(a, b, n):
    x = (b - a) / n
    suma = 0.0
    srodek = a + (b - a) / (2 * n)


    for i in range(0, n):
        suma += funkcja(srodek)
        srodek += x

    return suma * x

print("Podaj przedział [a, b]: ")
a = int(input(""))
b = int(input(""))
n = int(input("Podaj liczbę prostokątów: "))

if a >= b:
    print("To nie jest przedział!")
else:
    print("Pole figury wynosi: " + f"{pole(a, b, n): .2f}")
