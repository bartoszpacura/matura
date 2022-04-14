# 4.a

file = open("anagram.txt")

lines = []
wiersze = []


for line in file:
    lines.append(line.strip())

file.close()

for line in lines:
    temp = line.split()
    for i in range(len(temp) - 1):
        length = len(temp[i])
        length_2 = len(temp[i + 1])
        if length_2 != length:
            break
    else:
        wiersze.append(line)

save = open("wyniki-2010.txt", "a")
save.write("4.a\n")

for i in wiersze:
    print(i)
    save.write(i + "\n")

save.close()


# 4.b

file = open("anagram.txt")
lines = []
wiersze = []

for line in file:
    lines.append(line.strip())

for line in lines:
    temp = line.split()
    first = sorted(list(temp[0]))
    for word in temp:
        if sorted(list(word)) != first:
            break
    else:
        wiersze.append(line)

save = open("wyniki-2010.txt", "a")
save.write("\n4.b\n")

for i in wiersze:
    print(i)
    save.write(i + "\n")

save.close()

