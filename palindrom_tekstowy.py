# rozwiązanie 1.

# def palindrom(word):
#     length = len(word)
#
#     for j in range(length):
#         m = length - j - 1
#         if j < m:
#             if word[j] != word[m]:
#                 print("nie")
#                 break
#         else:
#             print("tak")
#             break
#
#
# zestawy = int(input("Ile wyrazów chcesz sprawdzić: "))
# counter = 0
#
# if zestawy > 10000:
#     print("Zbyt wiele wyrazów!")
#
# else:
#     for i in range(zestawy):
#         word = input("Wprowadź słowo: ")
#         m = len(word)
#         if 10 > m > 1:
#             pass
#         else:
#             flag = False
#             while flag is False:
#                 if m > 10:
#                     print("Za długie słowo!")
#                     word = input("Wprowadź słowo ponownie: ")
#                     m = len(word)
#
#                 elif m <= 1:
#                     print("Za krótkie słowo!")
#                     word = input("Wprowadź słowo ponownie: ")
#                     m = len(word)
#
#                 else:
#                     flag = True
#                     break
#
#         counter += 1
#
#         palindrom(word)
#


# rozwiązanie z wykorzystaniem boolean


# def palindrom(word):
#     length = len(word)
#
#     for j in range(length):
#         m = length - j - 1
#         if j < m:
#             if word[j] != word[m]:
#                 return False
#
#         else:
#             return True
#
#
# zestawy = int(input("Ile wyrazów chcesz sprawdzić: "))
# counter = 0
#
# if zestawy > 10000:
#     print("Zbyt wiele wyrazów!")
#
# else:
#     for i in range(zestawy):
#         word = input("Wprowadź słowo: ")
#         m = len(word)
#         if 10 > m > 1:
#             pass
#         else:
#             flag = False
#             while flag is False:
#                 if m > 10:
#                     print("Za długie słowo!")
#                     word = input("Wprowadź słowo ponownie: ")
#                     m = len(word)
#
#                 elif m <= 1:
#                     print("Za krótkie słowo!")
#                     word = input("Wprowadź słowo ponownie: ")
#                     m = len(word)
#
#                 else:
#                     flag = True
#                     break
#
#         counter += 1
#
#         b = palindrom(word)
#
#         if b is False:
#             print("nie")
#         if b is True:
#             print("tak")


# rozwiązanie 3. z linku http://www.algorytm.edu.pl/algorytmy-maturalne/palindrom.html

def palindrom(word):
    length = len(word)
    i = 0
    j = length - 1

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1

    return True


zestawy = int(input("Ile wyrazów chcesz sprawdzić: "))
counter = 0

if zestawy > 10000:
    print("Zbyt wiele wyrazów!")

else:
    for i in range(zestawy):
        word = input("Wprowadź słowo: ")
        m = len(word)
        if 10 > m > 1:
            pass
        else:
            flag = False
            while flag is False:
                if m > 10:
                    print("Za długie słowo!")
                    word = input("Wprowadź słowo ponownie: ")
                    m = len(word)

                elif m <= 1:
                    print("Za krótkie słowo!")
                    word = input("Wprowadź słowo ponownie: ")
                    m = len(word)

                else:
                    flag = True
                    break

        counter += 1

        b = palindrom(word)

        if b is False:
            print("nie")
        if b is True:
            print("tak")
