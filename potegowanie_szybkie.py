# rozwiązanie iteracyjne

# def potegowanie(a, n):
#     wynik = 1
#
#     while n > 0:
#         if n % 2 == 1:
#             wynik *= a
#
#         a *= a
#         n //= 2
#
#     return wynik
#
#
# a = int(input("Podaj podstawę: "))
# n = int(input("Podaj wykładnik: "))
#
# print(potegowanie(a, n))


# rozwiązanie rekurencyjne

def pot_sz(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return a * pot_sz(a, n - 1)

    return pot_sz(a, n // 2) * pot_sz(a, n // 2)



a = int(input("Podaj podstawę: "))
n = int(input("Podaj wykładnik: "))

print(pot_sz(a, n))
