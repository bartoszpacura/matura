# zamiana sąsiadujących liter

# def encryption(napis):
#     nowy_napis = list(napis)
#     for i in range(0, len(nowy_napis) - 1, 2):
#         nowy_napis[i], nowy_napis[i + 1] = nowy_napis[i + 1], nowy_napis[i]
#     nowy_napis = "".join(nowy_napis)
#     return nowy_napis
#
#
# napis = input("Podaj napis, który chcesz zaszyfrować:\n")
#
# print("Napis przed szyfrowaniem: " + napis)
#
# napis = encryption(napis)
# print(napis)
#
# print("Szyfrogram: " + napis)
#
# print("Teraz następuje deszyfrowanie...")
#
# napis = encryption(napis)
#
# print("Napis po deszyfrowaniu: " + napis)
#
#
# przesunięcie spółgłosek o jedno miejsce


def spolgloska(litera):
    match(litera):
        case "a" | "e" | "i" | "o" | "u" | "y":
            return 0

    return 1


def encryption(napis):
    word = list(napis)
    flag = 1
    nr = 0
    first = ""

    for i in range(len(word)):
        if spolgloska(word[i]):
            if flag:
                nr = i
                first = word[i]
                flag = 0
            else:
                word[i], first = first, word[i]
        if not flag:
            word[nr] = first

    word = "".join(word)
    return word


def decryption(napis):
    word = list(napis)
    flag = 1
    nr = 0
    first = ""

    for i in range(len(napis) - 1, -1, -1):
        if spolgloska(word[i]):
            if flag:
                nr = i
                first = word[i]
                flag = 0
            else:
                word[i], first = first, word[i]
        if not flag:
            word[nr] = first

    word = "".join(word)
    return word


napis = input("Podaj napis, który chcesz zaszyfrować:\n")

print("Napis przed szyfrowaniem: " + napis)

napis = encryption(napis)
print(napis)

print("Szyfrogram: " + str(napis))

print("Teraz następuje deszyfrowanie...")

napis = decryption(napis)

print("Napis po deszyfrowaniu: " + napis)
