n = []
numbers = int(input("How many numbers you want to sort?: "))

for number in range(numbers):
    n_a = int(input("Enter number: "))
    n.append(n_a)

for i in range(len(n) - 1):
    for j in range(0, len(n) - 1 - i):
        if n[j] > n[j + 1]:
            n[j], n[j + 1] = n[j + 1], n[j]

print("Sorted numbers: " + str(n))
