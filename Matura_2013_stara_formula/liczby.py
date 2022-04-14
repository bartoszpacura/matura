# 6.a

file = open("dane.txt")
numbers = []
numbers_answer = []

for i in file:
    numbers.append(i.strip())

file.close()

for n in numbers:
    if n[0] == n[len(n) - 1]:
        numbers_answer.append(n)

x = len(numbers_answer)
print(x)

save = open("wyniki_2013.txt", "a")
save.write("6.a " + str(x) + "\n")
save.close()

# 6.b

file = open("dane.txt")
numbers = []

for i in file:
    numbers.append(i.strip())

file.close()

counter = 0
for num in numbers:
    decimal = int(num, 8)
    if str(decimal)[0] == str(decimal)[len(str(decimal)) - 1]:
        counter += 1

print(counter)

save = open("wyniki_2013.txt", "a")
save.write("6.b " + str(counter) + "\n")
save.close()

# 6.c

file = open("dane.txt")
numbers = []
numbers_answer = []

for i in file:
    numbers.append(i.strip())

file.close()

for n in numbers:
    for i in range(len(n) - 1):
        if int(n[i + 1]) < int(n[i]):
            break
    else:
        numbers_answer.append(int(n))

sorted_list = sorted(numbers_answer)
minimum = sorted_list[0]
maximum = sorted_list[len(sorted_list) - 1]

c = len(numbers_answer)
print(c)
print(minimum)
print(maximum)

save = open("wyniki_2013.txt", "a")
save.write("6.c liczba: " + str(c) + ", najmniejsza liczba: " + str(minimum) + ", najwieksza liczba: " + str(maximum))
save.close()
