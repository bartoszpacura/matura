# 6.1.

file = open("dane.txt")

maximum = 0
minimum = 255

for wiersz in file:
    for number in wiersz.split():
        if int(number) > maximum:
            maximum = int(number)
        if int(number) < minimum:
            minimum = int(number)

print(maximum, minimum)

file.close()

save = open("wyniki_2017.txt", "a")
save.write(str(maximum) + " " + str(minimum) + "\n")
save.close()

# 6.2.


file = open("dane.txt")

numbers = []

for wiersz in file:
    numbers.append(wiersz.split())

file.close()

counter = 0
for wiersz in numbers:
    for i in range(0, 320):
        if wiersz[i] != wiersz[319 - i]:
            counter += 1
            break

print(counter)

save = open("wyniki_2017.txt", "a")
save.write(str(counter) + "\n")
save.close()

# 6.3.


def znajdz_kontrast(numbers, x, y):
    if x != 0:
        if abs(int(numbers[x][y]) - int(numbers[x - 1][y])) > 128:
            return True
    if x != 199:
        if abs(int(numbers[x][y]) - int(numbers[x + 1][y])) > 128:
            return True
    if y != 0:
        if abs(int(numbers[x][y]) - int(numbers[x][y - 1])) > 128:
            return True
    if y != 319:
        if abs(int(numbers[x][y]) - int(numbers[x][y + 1])) > 128:
            return True
    return False


file = open("dane.txt")

numbers = []

for i in file:
    numbers.append(i.split())

file.close()

counter = 0
for x in range(0, 200):
    for y in range(0, 320):
        if znajdz_kontrast(numbers, x, y):
            counter += 1

print(counter)

save = open("wyniki_2017.txt", "a")
save.write(str(counter) + "\n")
save.close()

# 6.4.


file = open("dane.txt")

numbers = []

for i in file:
    numbers.append(i.split())

counter = 1
counter_temp = 1
w = 0

while w < 200:
    for n in range(1, 200):
        if numbers[n][w] == numbers[n - 1][w]:
            counter_temp += 1
        else:
            if counter_temp > counter:
                counter = counter_temp
            counter_temp = 1
    w += 1

print(counter)

save = open("wyniki_2017.txt", "a")
save.write(str(counter) + "\n")
save.close()
