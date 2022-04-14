# 6.1


file = open("dane_6_1.txt")
words = []
encrypted = []

for i in file:
    words.append(i.strip())

file.close()


def encrypt(text):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + 107 - 65) % 26 + 65)
        else:
            result += chr((ord(char) + 107 - 97) % 26 + 97)

    return result


save = open("wyniki-2016-szyfr.txt", "a")
save.write("6.1.\n")

for i in range(len(words)):
    cipher = encrypt(words[i])
    encrypted.append(cipher)
    print(cipher)
    save.write(str(cipher) + "\n")

save.close()


# 6.2


file = open("dane_6_2.txt")
szyfrogramy = []
odszyfrowane = []

for i in file:
    szyfrogramy.append(i.strip().split())

file.close()

print(szyfrogramy)


def decrypt(text, key):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)

    return result


save = open("wyniki-2016-szyfr.txt", "a")
save.write("\n6.2.\n")

for i in range(len(szyfrogramy)):
    if len(szyfrogramy[i]) == 2:
        cipher = decrypt(szyfrogramy[i][0], int(szyfrogramy[i][1]))
        odszyfrowane.append(cipher)
        print(cipher)
        save.write(str(cipher) + "\n")
    else:
        odszyfrowane.append(szyfrogramy[i][0])
        print(szyfrogramy[i][0])
        save.write(str(szyfrogramy[i][0]) + "\n")

save.close()


# 6.3


file = open("dane_6_3.txt")
words = []
incorrect_keys = []

for i in file:
    words.append(i.strip().split())

file.close()


def key_checking(text_enc, text_dec):

    key_number = 0
    for i in range(len(text_enc)):
        char_enc = text_enc[i]
        char_dec = text_dec[i]

        key_check = (ord(char_enc) - ord(char_dec) - 65) % 26 + 65
        if i == 0:
            key_number = key_check
        elif key_check != key_number:
            incorrect_keys.append(text_enc)
            break
        else:
            continue


for i in range(len(words)):
    key_checking(words[i][0], words[i][1])


save = open("wyniki-2016-szyfr.txt", "a")
save.write("\n6.3.\n")

for word in incorrect_keys:
    print(word)
    save.write(str(word) + "\n")

save.close()