# Szybko zorientowałem się, że można zapisać to lepiej... w końcu zerknąłem do rozwiązania
#
# n = int(input(""))
# n_2 = n


# def mlp(list_mlp):
#     b = 1
#     for a in list_mlp:
#         b *= a
#     return b
#
#
# list_num = []
# if n > 1:
#     while n % 2 == 0:
#         n /= 2
#         list_num.append(2)
#
#     if n % 2 != 0:
#         while n != 1:
#             for numbers in range(2, n_2 + 1):
#                 if n % numbers == 0:
#                     n /= numbers
#                     list_num.append(numbers)
#
#     if len(list_num) > 1:
#         print(list_num)
#         print(mlp(list_num))
#
#     else:
#         print("Invalid value")
#
# else:
#     print("Invalid value")

from math import sqrt

n = int(input(""))
m = 2
sq = sqrt(n)

while n > 1 and m <= sq:
    while n % m == 0:
        print(m)
        n /= m
    m += 1
