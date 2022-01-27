numbers = []
how_many = int(input("How many numbers you want to sort?: "))

for number in range(how_many):
    n_a = int(input("Enter number: "))
    numbers.append(n_a)

for i in range(len(numbers)):
    min_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[min_index] > numbers[j]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(numbers)
