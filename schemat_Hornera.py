# rozwiązanie iteracyjne

# def wielomian(st, wsp, a):
#     suma = wsp[0]
#
#     for j in range(1, st + 1):
#         suma = suma * a + wsp[j]
#
#     return suma
#
#
# st = int(input("Podaj stopień wielomianu: "))
# wsp = []
#
# for i in range(st + 1):
#     w = input("Podaj współczynnik " + str(i + 1) + ": ")
#     wsp.append(int(w))
#
# a = int(input("Podaj argument: "))
#
# w = wielomian(st, wsp, a)
#
# print("W(" + str(a) + ") = " + str(w))


# rozwiązanie rekurencyjne

def wielomian(st, wsp, a):
    if st == 0:
        return wsp[0]

    return a * wielomian(st - 1, wsp, a) + wsp[st]


st = int(input("Podaj stopień wielomianu: "))
wsp = []

for i in range(st + 1):
    w = input("Podaj współczynnik " + str(i + 1) + ": ")
    wsp.append(int(w))

a = int(input("Podaj argument: "))

w = wielomian(st, wsp, a)

print("W(" + str(a) + ") = " + str(w))
