# rozwiązanie z użyciem funkcji sorted()

def anagram(a, b):

    if sorted(a.lower()) == sorted(b.lower()):
        print("Podane wyrazy są anagramami")
    else:
        print("Podane wyrazy nie są anagramami")


print("Podaj dwa wyrazy: ")
a = input("")
b = input("")
anagram(a, b)

# rozwiązanie z użyciem funkcji
# from collections import Counter
#
#
# def anagram(a, b):
#
#     if Counter(a.lower()) == Counter(b.lower()):
#         print("Podane wyrazy są anagramami")
#     else:
#         print("Podane wyrazy nie są anagramami")
#
#
# print("Podaj dwa wyrazy: ")
# a = input("")
# b = input("")
# anagram(a, b)
