# Rozwiazanie silowe

# n = int(input(""))
# k = 0
#
# if n > 0:
#     for number in range(1, n):
#         if n % number == 0:
#             k += number
#             if k == n:
#                 print("It is perfect number")
#         if number == n - 1 and k != n:
#             print("It is not perfect number")

from math import sqrt

n = int(input(""))
sq = round(sqrt(n))

list_num = []

if n > 0:
    for number in range(1, sq + 1):

        m = n / number
        m = int(m)

        if n % number == 0 and number > 1:
            list_num.append(number)
            list_num.append(m)

list_num = list(set(list_num))
suma = sum(list_num) + 1

if suma == n and suma != 1:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
