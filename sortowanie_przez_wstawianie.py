# przez wstawianie liniowe

numbers = []
how_many = int(input("How many numbers you want to sort?: "))

for number in range(how_many):
    n_a = int(input("Enter number: "))
    numbers.append(n_a)

for i in range(1, how_many):
    m = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > m:
        numbers[j + 1] = numbers[j]
        j -= 1

    print(j)
    numbers[j + 1] = m


print(numbers)

# binarne

