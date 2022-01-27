# przez wstawianie liniowe
#
# numbers = []
# how_many = int(input("How many numbers you want to sort?: "))
#
# for number in range(how_many):
#     n_a = int(input("Enter number: "))
#     numbers.append(n_a)
#
# for i in range(1, how_many):
#     m = numbers[i]
#     j = i - 1
#     while j >= 0 and numbers[j] > m:
#         numbers[j + 1] = numbers[j]
#         j -= 1
#
#     print(j)
#     numbers[j + 1] = m
#
# print(numbers)

# binarne sortowanie przez wstawianie

def binary_search(arr, key, start, end):
    if end - start <= 1:
        if key < arr[start]:
            return start - 1
        else:
            return start
    mid = (start + end) // 2
    if arr[mid] < key:
        return binary_search(arr, key, mid, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid)
    else:
        return mid


def insertion_sort(arr):
    for i in range(1, len(arr)):
        m = arr[i]
        pos = binary_search(arr, m, 0, i) + 1
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        arr[pos] = m


numbers = []
how_many = int(input("How many numbers you want to sort?: "))

for number in range(how_many):
    n_a = int(input("Enter number: "))
    numbers.append(n_a)

insertion_sort(numbers)
print(numbers)
