def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        print("L: ", l)
        print("R: ", r)
        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

        print("Array: ", arr)


numbers = []

n = int(input("How many numbers you want to sort?: "))

for number in range(n):
    n_a = int(input("Enter number: "))
    numbers.append(n_a)

print(numbers)
merge_sort(numbers)
print(numbers)



# tutaj próbowałem zrobić sposobem, jak gość z tego filmiku https://www.youtube.com/watch?v=HFpo5ox11aA
# cały czas nie działa i już w sumie sam nie wiem dlaczego

# def merge_sort(arr, left, right):
#     if left < right:
#         mid = left + (right - left) // 2
#
#         merge_sort(arr, left, mid)
#         merge_sort(arr, mid + 1, right)
#         merge(arr, left, mid, right)
#
#
# def merge(arr, left, mid, right):
#
#     for i in range(left, right + 1):
#         numbers_temp[i] = arr[i]
#
#     l = left
#     r = mid + 1
#     k = left
#
#     while l <= mid and r <= right:
#         if numbers_temp[l] <= numbers_temp[r]:
#             arr[k] = numbers_temp[l]
#             l += 1
#         else:
#             arr[k] = numbers_temp[r]
#             r += 1
#         k += 1
#
#     while l <= mid:
#         arr[k] = numbers_temp
#         l += 1
#
#
# numbers_temp = []
#
# numbers = []
# n = int(input("How many numbers you want to sort?: "))
#
# for number in range(n):
#     n_a = int(input("Enter number: "))
#     numbers.append(n_a)
#
# print(numbers)
# merge_sort(numbers, 0, n - 1)
# print(numbers)
