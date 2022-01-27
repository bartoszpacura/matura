numbers = []
n = int(input("How many numbers you want to sort?: "))


def quick_sort(tab, left, right):
    i = left
    j = right
    pivot = tab[(left + right) // 2]

    while i <= j:
        while tab[i] < pivot:
            i += 1
        while tab[j] > pivot:
            j -= 1
        if i <= j:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1

    if j > left:
        quick_sort(tab, left, j)
    if i < right:
        quick_sort(tab, i, right)


for number in range(n):
    n_a = int(input("Enter number: "))
    numbers.append(n_a)

quick_sort(numbers, 0, n-1)
print(numbers)
