# 4.1.

file = open("instrukcje.txt")

counter = 0
for i in file:
    a = i.split()
    if a[0] == "DOPISZ":
        counter += 1
    elif a[0] == "USUN":
        counter -= 1

file.close()

save = open("wyniki_21.txt", "a")
save.write(str(counter) + "\n")
save.close()


# 4.2.

file = open("instrukcje.txt")

tab = []

for i in file:
    a = i.split()
    tab.append(a[0])

counter = 1
counter_max = 1
instruction = ""

for i in range(1, len(tab)):
    if tab[i] == tab[i - 1]:
        counter += 1
    else:
        if counter_max < counter:
            counter_max = counter
            instruction = tab[i - 1]
        counter = 1

file.close()


save = open("wyniki_21.txt", "a")
save.write(str(counter_max) + " " + str(instruction) + "\n")
save.close()


# 4.3.

file = open("instrukcje.txt")
tab = []

for i in file:
    tab.append(i.split())

tab_dopisz = []

for i in tab:
    if i[0] == "DOPISZ":
        tab_dopisz.append(i[1])

letter = ""
letter_max = ""
counter = 0
counter_max = 0

for i in tab_dopisz:
    letter = i
    for j in tab_dopisz:
        if j == i:
            counter += 1
    if counter_max < counter:
        counter_max = counter
        letter_max = letter
    counter = 0

print(letter_max, counter_max)

file.close()

save = open("wyniki_21.txt", "a")
save.write(str(letter_max) + " " + str(counter_max) + "\n")
save.close()


# 4.4.


file = open("instrukcje.txt")

tab = []

for i in file:
    tab.append(i.split())

word = []

for instruction in tab:
    if instruction[0] == "DOPISZ":
        word.append(instruction[1])
    elif instruction[0] == "ZMIEN":
        word[len(word) - 1] = instruction[1]
    elif instruction[0] == "USUN":
        word.pop()
    elif instruction[0] == "PRZESUN":
        for i in word:
            if i == instruction[1]:
                index = word.index(i)
                a = ord(word[index]) + 1
                if a > 90:
                    a -= 26
                word[index] = chr(a)
                break

word = "".join(word)

print(word)

file.close()

save = open("wyniki_21.txt", "a")
save.write(str(word))
save.close()
