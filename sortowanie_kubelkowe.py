def bucket_sort(array):
    largest = max(array)
    length = len(array)
    size = largest / length

    buckets = []

    # buckets = [[] for i in range(length)]
    for i in range(length):
        buckets.append([])

    for i in range(length):
        index = int(array[i] / size)
        print(index)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])

    for i in range(length):
        buckets[i] = sorted(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


numbers = []
n = int(input("How many numbers you want to sort?: "))

for number in range(n):
    n_a = int(input("Enter number: "))
    print(n_a)
    numbers.append(n_a)

print("Sorted Array in descending order is")
print(bucket_sort(numbers))
