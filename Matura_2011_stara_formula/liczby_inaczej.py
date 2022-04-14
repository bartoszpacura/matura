# 6.a

file = open("liczby.txt")
numbers_decimal = []

for i in file:
    number_binary = i.strip()
    numbers_decimal.append(int(number_binary, 2))

file.close()

counter = 0
for i in numbers_decimal:
    if i % 2 == 0:
        counter += 1

print(counter)

save = open("wyniki_2011.txt", "a")
save.write("6.a " + str(counter) + "\n")

# 6.b

numbers_decimal.sort(reverse=True)
print(numbers_decimal[0])

save.write("6.b " + str(numbers_decimal[0]) + "\n")

# 6.c

file = open("liczby.txt")
numbers_binary = []
numbers_decimal = []

for i in file:
    numbers_binary.append(i.strip())

file.close()

counter_nine = 0
for i in numbers_binary:
    if len(i.strip()) == 9:
        counter_nine += 1
        numbers_decimal.append(i)

print(counter_nine)

sum = "0"
for i in numbers_decimal:
    sum = bin(int(sum, 2) + int(i, 2))

print(sum[2:])

save.write("6.c " + str(counter_nine) + ", " + str(sum[2:]))
save.close()