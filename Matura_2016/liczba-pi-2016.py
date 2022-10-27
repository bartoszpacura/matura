# 4.1.


def wsp(number, lista_x, lista_y, lista_okrag):
    counter_okrag = 0
    counter_wew = 0
    counter_zew = 0

    for i in range(0, number):
        a = 200
        b = 200
        if (int(lista_x[i]) - 200) ** 2 + (int(lista_y[i]) - 200) ** 2 == 200 ** 2:
            lista_okrag.append((int(lista_x[i]), int(lista_y[i])))
            counter_okrag += 1

        elif (int(lista_x[i]) - 200) ** 2 + (int(lista_y[i]) - 200) ** 2 < 200 ** 2:
            counter_wew += 1
        else:
            counter_zew += 1

    lista_counter = [counter_okrag, counter_wew, counter_zew]

    return lista_counter


lista_x = []
lista_y = []
lista_okrag = []

file = open("punkty.txt")

for line in file.readlines():
    p = line.split(" ")
    lista_x.append(p[0])
    lista_y.append(p[1])

counter = wsp(10000, lista_x, lista_y, lista_okrag)

print(lista_okrag)
file.close()

save = open("wynik5.txt", "a")
save.write("Punkty nalezace do brzegu kola: " + str(lista_okrag[0]) + " " + str(lista_okrag[1]) + "\n")
save.write("Liczba punktow nalezacych do wnetrza kola: " + str(counter[1]) + "\n")
save.close()


# 4.2.


def wartosc_pi(counter, counter_1):
    nk_n = counter / counter_1
    p_k = 400 ** 2
    r_k = 200 ** 2

    pi = nk_n * p_k / r_k
    return pi


file = open("punkty.txt")

lista_x = []
lista_y = []
lista_okrag = []

for line in file.readlines():
    p = line.split(" ")
    lista_x.append(p[0])
    lista_y.append(p[1])

counter_1 = wsp(1000, lista_x, lista_y, lista_okrag)
pi_1 = wartosc_pi(counter_1[0] + counter_1[1], 1000)

counter_2 = wsp(5000, lista_x, lista_y, lista_okrag)
pi_2 = wartosc_pi(counter_2[0] + counter_2[1], 5000)

counter_3 = wsp(10000, lista_x, lista_y, lista_okrag)
pi_3 = wartosc_pi(counter_3[0] + counter_3[1], 10000)

file.close()

print(pi_1, pi_2, pi_3)

save = open("wynik5.txt", "a")
save.write("\n" + str(pi_1) + "\n" + str(pi_2) + "\n" + str(pi_3) + "\n" + "\n")
save.close()

# 4.3.


import math
import matplotlib.pyplot as plt

lista_x = []
lista_y = []
lista_okrag = []
bledy_bez = []
bledy_bez_save = []

file = open("punkty.txt")

for line in file.readlines():
    p = line.split(" ")
    lista_x.append(p[0])
    lista_y.append(p[1])


for i in range(1, 1701):
    x = wsp(i, lista_x, lista_y, lista_okrag)
    pi_b = wartosc_pi(x[0] + x[1], i)
    e = abs(math.pi - pi_b)
    bledy_bez.append(e)


plt.plot(bledy_bez)
plt.show()

for i in range(999, 1700):
    bledy_bez_save.append(format(bledy_bez[i], '.4f'))

file.close()


print(bledy_bez_save)

save = open("wynik5.txt", "a")
for i in range(len(bledy_bez_save)):
    save.write(str(bledy_bez_save[i]) + "\n")
save.close()
