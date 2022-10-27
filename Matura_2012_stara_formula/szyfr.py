# 4.1.


niezaszyfrowane = open("tj.txt")
niezaszyfrowane_lista = []

for i in niezaszyfrowane:
    niezaszyfrowane_lista.append(i.strip())

niezaszyfrowane.close()

klucze = open("klucze1.txt")
klucze_lista = []

for i in klucze:
    klucze_lista.append(i.strip())

klucze.close()


def encrypt(text, key):
    result = ""

    for i in range(len(text)):
        temp = (ord(text[i]) + ord(key[i % len(key)]) - 64)
        if temp > 90:
            temp -= 26
        result += chr(temp)

    return result


save = open("wyniki_2012.txt", "a")
save.write("4.1.\n")

for i, j in zip(niezaszyfrowane_lista, klucze_lista):
    r = encrypt(i, j)
    print(r)
    save.write(r + "\n")

save.close()

# 4.2.


niezaszyfrowane = open("sz.txt")
niezaszyfrowane_lista = []

for i in niezaszyfrowane:
    niezaszyfrowane_lista.append(i.strip())

niezaszyfrowane.close()

klucze = open("klucze2.txt")
klucze_lista = []

for i in klucze:
    klucze_lista.append(i.strip())

klucze.close()


def encrypt(text, key):
    result = ""

    for i in range(len(text)):
        temp = (ord(text[i]) - ord(key[i % len(key)]) + 64)
        if temp < 65:
            temp += 26
        result += chr(temp)

    return result


save = open("wyniki_2012.txt", "a")
save.write("\n4.2.\n")

for i, j in zip(niezaszyfrowane_lista, klucze_lista):
    r = encrypt(i, j)
    print(r)
    save.write(r + "\n")

save.close()
