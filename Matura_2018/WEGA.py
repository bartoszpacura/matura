# 4.1.


file = open("sygnaly.txt")

words = []
przeslanie = []

for i in file:
    words.append(i.strip())

counter = 39
while counter < 1000:
    word = words[counter]
    przeslanie.append(word[9])
    counter += 40

sentence = "".join(przeslanie)

print(sentence)

file.close()

save = open("wyniki_2018.txt", "a")
save.write("4.1. " + str(sentence) + "\n")
save.close()


# 4.2.


file = open("sygnaly.txt")

letters = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False,
           'F': False, 'G': False, 'H': False, 'I': False, 'J': False,
           'K': False, 'L': False, 'M': False, 'N': False, 'O': False,
           'P': False, 'Q': False, 'R': False, 'S': False, 'T': False,
           'U': False, 'V': False, 'W': False, 'X': False, 'Y': False, 'Z': False}

max = ""
counter = 0
for word in file:
    letters_copy = letters.copy()
    counter_in = 0
    for j in range(len(word)):
        letter = word[j]
        if letter in letters_copy:
            if letters_copy[letter] is False:
                counter_in += 1
            letters_copy[letter] = True
        if j == len(word) - 1 and counter_in > counter:
            counter = counter_in
            max = word

print(max)
print(counter)


file.close()

save = open("wyniki_2018.txt", "a")
save.write("\n" + "4.2. " + max + str(counter) + "\n")
save.close()


# 4.3.


file = open("sygnaly.txt")

list_ut = []

for line in file.readlines():
    line = line.strip()
    line_sort = "".join(sorted(line))
    if ord(line_sort[len(line_sort) - 1]) - ord(line_sort[0]) <= 10:
        list_ut.append(line)

print(list_ut)

file.close()

save = open("wyniki_2018.txt", "a")
save.write("\n" + "4.3. \n")
for i in list_ut:
    save.write(i + "\n")
save.close()
