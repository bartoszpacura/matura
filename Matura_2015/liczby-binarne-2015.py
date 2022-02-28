# 4.1.


liczby_binarne_wiecej_zer = []

file = open("liczby.txt")

for line in file.readlines():
    a = 0
    b = 0
    for i in line:
        if i == '0':
            a += 1
        elif i == '1':
            b += 1
    if a > b:
        liczby_binarne_wiecej_zer.append(line.strip())

file.close()

wynik_1 = len(liczby_binarne_wiecej_zer)
print(wynik_1)

save = open("wynik4.txt", "a")
save.write(str(wynik_1) + "\n")
save.close()



# 4.2.


liczby_binarne_podzielne_przez_dwa = []
liczby_binarne_podzielne_przez_osiem = []

file = open("liczby.txt")

for line in file.readlines():
    line_t = line.strip()
    if line[len(line_t) - 1] == '0':
        liczby_binarne_podzielne_przez_dwa.append(line_t)

file.close()

wynik_2 = len(liczby_binarne_podzielne_przez_dwa)
print(wynik_2)

file = open("liczby.txt")

for line in file.readlines():
    line_w = line.strip()
    if line[len(line_w) - 1] == '0' and line[len(line_w) - 2] == '0' and line[len(line_w) - 3] == '0':
        liczby_binarne_podzielne_przez_osiem.append(line_w)

file.close()

wynik_3 = len(liczby_binarne_podzielne_przez_osiem)
print(wynik_3)

save = open("wynik4.txt", "a")
save.write(str(wynik_2) + "\n" + str(wynik_3) + "\n")
save.close()



# 4.3.


list_max_min = []


def zamiana(n):
    counter = len(n) - 1
    final = 0
    for i in n:
        a = int(i)
        final += a * pow(2, counter)
        counter -= 1
    return final


file = open("liczby.txt")


for i in file.readlines():
    zam = zamiana(i.strip())
    list_max_min.append(zam)

maximum = 0
maximum_index = 0
for i in range(len(list_max_min)):
    if list_max_min[i] > maximum:
        maximum = list_max_min[i]
        maximum_index = i

minimum = maximum
minimum_index = 0
for i in range(len(list_max_min)):
    if list_max_min[i] < minimum:
        minimum = list_max_min[i]
        minimum_index = i

file.close()

wynik_4 = minimum_index + 1
wynik_5 = maximum_index + 1

print(wynik_4)
print(wynik_5)

save = open("wynik4.txt", "a")
save.write(str(wynik_4) + ", " + str(wynik_5))
save.close()
