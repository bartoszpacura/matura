# 6.1.

# file = open("dane.txt")
#
# dane = []
#
# max = 0
# min = 255
#
# for line in file:
#     temp = line.split()
#     dane.append([int(x) for x in temp])
#
# for i in dane:
#     for j in i:
#         if j > max:
#             max = j
#         if j < min:
#             min = j
#
# print("Najjaśniejszy piksel: " + str(max))
# print("Najciemniejszy piksel: " + str(min))
#
# file.close()




# 6.2.

# dane = []
# file = open("dane.txt")
# counter = 0
#
#
# for line in file.readlines():
#     dane.append(line.split())
#
# for line in dane:
#     for i in range(len(line) // 2):
#         if line[i] != line[len(line) - i - 1]:
#             counter += 1
#             break
#
# print("Najmniejsza liczba wierszy, jaką należy usunąć to: " + str(counter))
#
# file.close()




# 6.3.

# dane = []
# file = open("dane.txt")
# counter = 0
# tab_id = []
#
# for line in file:
#     temp = line.split()
#     dane.append([int(x) for x in temp])


# do przeanalizowania

import math


def nearContrasting(x, y, all):
    if x != 0:
        if math.fabs(all[x][y] - all[x - 1][y]) > 128:
            return True
    if x != 199:
        if math.fabs(all[x][y] - all[x + 1][y]) > 128:
            return True
    if y != 319:
        if math.fabs(all[x][y] - all[x][y + 1]) > 128:
            return True
    if y != 0:
        if math.fabs(all[x][y] - all[x][y - 1]) > 128:
            return True
    return False


file = open("dane.txt", "r").read().split('\n')
dane = [[0 for x in range(320)] for y in range(200)]
counter = 0
contrasting = 0
for line in file:
    if len(line.split(" ")) < 2 or len(line.split(" ")[1]) < 1:
        continue
    points = line.split(" ")
    for i in range(320):
        dane[counter][i] = int(points[i])
    counter += 1
for i in range(200):
    for j in range(320):
        if nearContrasting(i, j, dane):
            contrasting += 1
print("Punktów kontrastujących: " + str(contrasting))



# 6.4.

