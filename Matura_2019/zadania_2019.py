# 4.1.

def potega_trojki(n):
    if n <= 0:
        return False
    if n % 3 == 0:
        return potega_trojki(n // 3)
    if n == 1:
        return True
    return False


file = open("liczby.txt")

numbers = []

for number in file:
    numbers.append(int(number))

counter = 0
for n in numbers:
    if potega_trojki(n):
        counter += 1

print(counter)

file.close()

save = open("wyniki_2019.txt", "a")
save.write("4.1. " + str(counter) + "\n")
save.close()

# 4.2.

file = open("liczby.txt")

numbers = []
numbers_silnia_rowna_liczbie = []

for n in file:
    numbers.append(n.strip())

for i in numbers:
    numbers_silnia = []
    numbers_silnia_po_obliczeniu = []
    p = list(i)
    for j in p:
        numbers_silnia.append(int(j))
    for k in numbers_silnia:
        silnia = 1
        for l in range(1, k + 1):
            silnia *= l
        numbers_silnia_po_obliczeniu.append(silnia)

    silnia_po_dodaniu = 0

    for m in numbers_silnia_po_obliczeniu:
        silnia_po_dodaniu += m

    if silnia_po_dodaniu == int(i):
        numbers_silnia_rowna_liczbie.append(int(i))

print(numbers_silnia_rowna_liczbie)

file.close()

save = open("wyniki_2019.txt", "a")
save.write("4.2. ")
for i in numbers_silnia_rowna_liczbie:
    save.write(str(i) + " ")
save.write("\n")
save.close()


# 4.3.

file = open("liczby.txt")

numbers = []

for i in file:
    numbers.append(int(i.strip()))

file.close()

# szukanie maximum

maximum = 0

for j in numbers:
    if j > maximum:
        maximum = j

# szukanie najdłuższego ciągu

counter = 0
counter_max = 0
pierwsza_liczba = 0
pierwsza_liczba_temp = 0
dzielnik = 0
dzielnik_temp = 0

for n in range(2, maximum + 1):
    for m in numbers:
        if m % n == 0:
            counter += 1
            if counter == 1:
                pierwsza_liczba_temp = m
                dzielnik_temp = n
        else:
            if counter_max <= counter:
                counter_max = counter
                pierwsza_liczba = pierwsza_liczba_temp
                dzielnik = dzielnik_temp
            counter = 0

print(pierwsza_liczba, counter_max, dzielnik)


save = open("wyniki_2019.txt", "a")
save.write("4.3. " + "pierwsza liczba ciagu: " + str(pierwsza_liczba)
           + ", dlugosc: " + str(counter_max) + ", najwiekszy wspolny dzielnik " + str(dzielnik))
save.close()
