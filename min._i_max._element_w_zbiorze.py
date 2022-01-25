# Znajdowanie najmniejszego lub największego elementu w zbiorze

# bez użycia tablicy

# check = input("max whether min number: ")
#
# if check == "max":
#     numbers = int(input("How many numbers you want to enter?: "))
#     m = 0
#
#     for n in range(1, numbers + 1):
#         a = int(input("Enter the number: "))
#         if m < a:
#             m = a
#
#     print("max number is: " + str(m))
#
# elif check == "min":
#     numbers = int(input("How many numbers you want to enter?: "))
#     m = 0
#
#     for n in range(1, numbers + 1):
#         a = int(input("Enter the number: "))
#         if m > a:
#             m = a
#
#     print("min number is: " + str(m))


# z użyciem tablicy

# check = input("max whether min number: ")
# num_a = []
#
# if check == "max":
#     numbers = int(input("How many numbers you want to enter?: "))
#
#     for n in range(1, numbers + 1):
#         a = int(input("Enter the number: "))
#         num_a.append(a)
#
#     print(num_a)
#     print("max number is: " + str(max(num_a)))
#
# elif check == "min":
#     numbers = int(input("How many numbers you want to enter?: "))
#
#     for n in range(1, numbers + 1):
#         a = int(input("Enter the number: "))
#         num_a.append(a)
#
#     print(num_a)
#     print("min number is: " + str(min(num_a)))


# z użyciem tablicy sposobem z rozwiązania

# check = input("max whether min number: ")
# num_a = []
#
# if check == "max":
#     numbers = int(input("How many numbers you want to enter?: "))
#
#     for n in range(1, numbers + 1):
#         a = int(input("Enter the number: "))
#         num_a.append(a)
#
#     m = num_a[0]
#
#     for i in num_a:
#         if m < i:
#             m = i
#
#     print(num_a)
#     print("max number is: " + str(m))
#
# elif check == "min":
#     numbers = int(input("How many numbers you want to enter?: "))
#
#     for n in range(1, numbers + 1):
#         a = int(input("Enter the number: "))
#         num_a.append(a)
#
#     m = num_a[0]
#
#     for i in num_a:
#         if m > i:
#             m = i
#
#     print(num_a)
#     print("min number is: " + str(m))


# Znajdowanie jednocześnie min i max bez użycia tablicy

# how_many = int(input("How many numbers you want to enter?: "))
#
# max_num = 0
# min_num = 0
# counter = 4
#
#
# num_1 = int(input("Enter the number: "))
# num_2 = int(input("Enter the number: "))
#
# if num_1 > num_2:
#     max_num = num_1
#     min_num = num_2
# elif num_1 < num_2:
#     min_num = num_1
#     max_num = num_2
#
# while counter <= how_many:
#     num_1 = int(input("Enter the number: "))
#     num_2 = int(input("Enter the number: "))
#
#     if num_1 > num_2:
#         if num_1 > max_num:
#             max_num = num_1
#         if num_2 < min_num:
#             min_num = num_2
#
#     elif num_1 < num_2:
#         if num_2 > max_num:
#             max_num = num_2
#         if num_1 < min_num:
#             min_num = num_1
#
#     counter += 2
#
# if how_many > 1 and how_many % 2 == 1:
#     num_1 = int(input("Enter the number: "))
#     if num_1 > max_num:
#         max_num = num_1
#     elif num_1 < min_num:
#         min_num = num_1
#
#
# print("max number is: " + str(max_num) + " min number is: " + str(min_num))


# Znajdowanie jednocześnie min i max z tablicą

def min_max_list(list_n, user_hm):
    max_num = 0
    min_num = 0
    i = 2

    if list_n[0] > list_n[1]:
        max_num = list_n[0]
        min_num = list_n[1]
    elif list_n[0] < list_n[1]:
        min_num = list_n[0]
        max_num = list_n[1]

    # for i in range(2, how_many - 1):
    while i + 2 <= how_many:
        if list_n[i] > list_n[i+1]:
            if list_n[i] > max_num:
                max_num = list_n[i]
            if list_n[i+1] < min_num:
                min_num = list_n[i+1]

        elif list_n[i] < list_n[i+1]:
            if list_n[i+1] > max_num:
                max_num = list_n[i+1]
            if list_n[i] < min_num:
                min_num = list_n[i]

        i += 2

    if user_hm % 2 == 1:

        if list_n[how_many-1] > max_num:
            max_num = list_n[how_many-1]
        elif list_n[how_many-1] < min_num:
            min_num = list_n[how_many-1]

    print("max number is: " + str(max_num) + " min number is: " + str(min_num))


numbers_list = []

how_many = int(input("How many numbers you want to enter?: "))

if how_many > 1:
    for n in range(0, how_many):
        a = int(input("Enter the number: "))
        numbers_list.append(a)

min_max_list(numbers_list, how_many)
