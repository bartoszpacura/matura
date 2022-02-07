def funkcja(x):
    return x * x + x + 2

def pole(a, b, n):
    h = (b - a) / n
    suma = 0.0
    podstawa_a = funkcja(a)

    for i in range(1, n + 1):
        podstawa_b = funkcja(a + h * i)
        suma += (podstawa_a + podstawa_b)
        podstawa_a = podstawa_b

    return (suma / 2) * h

print("Podaj przedział [a, b]: ")
a = int(input(""))
b = int(input(""))
n = int(input("Podaj liczbę trapezów: "))

if a >= b:
    print("To nie jest przedział!")
else:
    print("Pole figury wynosi: " + f"{pole(a, b, n): .2f}")
