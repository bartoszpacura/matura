# 4.1

file = open("galerie.txt")
lista_file = []
panstwa = set()
lista_z_liczba = []

for i in file:
    lista_file.append(i.strip())

file.close()

for i in lista_file:
    temp = i.split()
    panstwa.add(temp[0])

for i in panstwa:
    counter = 0
    for j in lista_file:
        temp = j.strip().split()
        if temp[0] == i:
            counter += 1
    temp_list = [i, counter]
    lista_z_liczba.append(temp_list)

print(lista_z_liczba)

save = open("wyniki-2021-pm.txt", "a")
save.write("4.1. " + "\n")
for i in lista_z_liczba:
    save.write(str(i[0]) + " " + str(i[1]) + "\n")
save.close()

# 4.2.

# a

file = open("galerie.txt")
lista_file = []
odpowiedz_lista = []

for i in file:
    lista_file.append(i.strip().split())

file.close()

save = open("wyniki-2021-pm.txt", "a")
save.write("\n4.2. a)\n")


for wiersz in lista_file:
    powierzchnia_calkowita = 0
    counter = 0
    for slowo in range(2, len(wiersz) - 1, 2):
        if int(wiersz[slowo]) < 1:
            break
        else:
            powierzchnia_calkowita += int(wiersz[slowo]) * int(wiersz[slowo + 1])
            counter += 1
    print(wiersz[1], powierzchnia_calkowita, counter)
    odpowiedz_lista.append([wiersz[1], powierzchnia_calkowita, counter])
    save.write(wiersz[1] + " " + str(powierzchnia_calkowita) + " " + str(counter) + "\n")


save.close()

# b

odpowiedz_lista.sort(key=lambda x: int(x[1]), reverse=True)

najwieksza = [odpowiedz_lista[0][0], odpowiedz_lista[0][1]]
najmniejsza = [odpowiedz_lista[len(odpowiedz_lista) - 1][0], odpowiedz_lista[len(odpowiedz_lista) - 1][1]]

print(najwieksza, najmniejsza)

save = open("wyniki-2021-pm.txt", "a")
save.write("\n4.2. b)\n" + str(najwieksza) + "\n" + str(najmniejsza) + "\n")
save.close()


# 4.3.

file = open("galerie.txt")
lista_file = []
lista_odpowiedz = []

for i in file:
    lista_file.append(i.strip().split())

file.close()

for wiersz in lista_file:
    lokale = set()
    for slowo in range(2, len(wiersz) - 1, 2):
        if int(wiersz[slowo]) < 1:
            break
        else:
            powierzchnia_lokalu = int(wiersz[slowo]) * int(wiersz[slowo + 1])
            lokale.add(powierzchnia_lokalu)
    lista_odpowiedz.append([wiersz[1], len(lokale)])

lista_odpowiedz.sort(key=lambda x: int(x[1]), reverse=True)

maximum = lista_odpowiedz[0]
minimum = lista_odpowiedz[len(lista_odpowiedz) - 1]

print(maximum, minimum)

save = open("wyniki-2021-pm.txt", "a")
save.write("\n4.3. " + "\n" + str(maximum) + "\n" + str(minimum))
save.close()



