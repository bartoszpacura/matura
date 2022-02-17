# proste rozwiązanie

# a = input("Wprowadź tekst: ")
# b = input("Wprowadź wzorzec: ")
#
# if a in b:
#     print("Wzorzec znaleziony")
# else:
#     print("Wzorzec nie znaleziony")


# rozwiązanie 2. http://www.algorytm.edu.pl/algorytmy-maturalne/wyszukiwanie-wzorca-w-tekscie.html

def szukaj(wzorzec, tekst):
    for i in range(0, (len(tekst) + 1) - len(wzorzec)):
        c = 0
        for j in range(0, len(wzorzec)):
            if wzorzec[j] != tekst[i + c]:
                break
            if j == len(wzorzec) - 1:
                return i + 1
            c += 1

    return -1


a = input("Wprowadź tekst: ")
b = input("Wprowadź wzorzec: ")

pos = szukaj(b, a)

if pos == -1:
    print("Wzorzec nie znaleziony")
else:
    print("Wzorzec znaleziony na " + str(pos) + " pozycji")
