# 5.a

import math


def znajdz_liczby_pierwsze(n):
    s = int(math.sqrt(n))
    for i in range(2, s + 1):
        if n % i == 0:
            return False
    return True


file = open("NAPIS.TXT")
words = []
napisy_pierwsze = []

for i in file:
    words.append(i.strip())

file.close()

for word in words:
    counter = 0
    for letter in word:
        counter += int(ord(letter))
    if znajdz_liczby_pierwsze(counter):
        napisy_pierwsze.append(counter)

c = len(napisy_pierwsze)
print(c)

save = open("matura-2014-wyniki.txt", "a")
save.write("5.a " + str(c) + "\n")
save.close()

# 5.b

file = open("NAPIS.TXT")
words = []
napisy_rosnace = []

for i in file:
    words.append(i.strip())

file.close()

save = open("matura-2014-wyniki.txt", "a")
save.write("5.b\n")

for word in words:
    for i in range(len(word) - 1):
        if ord(word[i + 1]) <= ord(word[i]):
            break
    else:
        napisy_rosnace.append(word)
        save.write(word + "\n")

print(napisy_rosnace)

save.close()

# 5.c

file = open("NAPIS.TXT")
words = []
words_answer = []

for i in file:
    words.append(i.strip())

file.close()

save = open("matura-2014-wyniki.txt", "a")
save.write("5.c\n")

for word in words:
    counter = words.count(word)

    if counter > 1:
        if words_answer.count(word) == 0:
            words_answer.append(word)
            save.write(word + "\n")

print(words_answer)

save.close()
