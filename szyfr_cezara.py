def encrypt(text, key):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result


def decrypt(text, key):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)

    return result


text = input("Wprowadź tekst do zaszyfrowania: ")
key = int(input("Podaj klucz z przedziału [-26,26]: "))

print("Klucz: " + str(key))
cipher = encrypt(text, key)
print("Szyfr: " + cipher)

plaintext = decrypt(cipher, key)

print("Tekst jawny po deszyfrowaniu: " + plaintext)
