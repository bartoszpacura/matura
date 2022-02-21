# odległość między wierzchołkami drzewa

# print("Wprowadź numer pierwszego wierzchołka: ")
# a = int(input(""))
# b = int(input(""))
# counter = 0
#
# while a != b:
#     if a > b:
#         a //= 2
#     else:
#         b //= 2
#
#     counter += 1
#
# print("Odległość między wierzchołkami wynosi: " + str(counter))

# drzewo binarne z tutorialu Zelenta

array = [None]
empty = [None]

for i in range(1, 16):
    array.append("_")
    empty.append(True)


while True:
    number = int(input("Jaką liczbę dodać do drzewa: "))
    if array[1] == "_":
        array[1] = number
        empty[1] = False
    else:
        w = 1
        flag = False

        while flag is False:
            if w > 15:
                print("Potrzebne większe drzewo!")
                flag = True

            elif empty[w]:
                flag = True
                array[w] = number
                empty[w] = False
            elif number <= array[w]:
                w *= 2
            else:
                w = w * 2 + 1

    # trzeba jeszcze napisać, w jaki sposób mają pojawiać się poszczególne komórki
    print(array[1])
    print(array[2], array[3])
    print(array[4], array[5], array[6], array[7])
    print(array[8], array[9], array[10], array[11], array[12], array[13], array[14], array[15])
