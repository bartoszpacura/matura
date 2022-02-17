# def number(num):
#     return "0" <= num <= "9"
#
#
# def operator(op):
#     if op == "+":
#         return "+"
#     elif op == "-":
#         return "-"
#     elif op == "*":
#         return "*"
#     elif op == "/":
#         return "/"
#
#
# def dzialanie(b, a, op):
#     if op == "+":
#         return b + a
#     elif op == "-":
#         return b - a
#     elif op == "*":
#         return b * a
#     elif op == "/":
#         return b // a
#
#
# stack = []
# text = input("")
# flag = False
#
# for i in range(len(text)):
#     if number(text[i]):
#         stack.append(int(text[i]))
#     else:
#         if operator(text[i]):
#             if len(stack) < 2:
#                 print("Nieprawidłowe wyrażenie ONP")
#                 flag = True
#                 break
#             else:
#                 a = stack.pop()
#                 b = stack.pop()
#                 stack.append(dzialanie(b, a, text[i]))
#
# if len(stack) != 1:
#     print("Nieprawidłowe wyrażenie ONP")
# elif flag is False:
#     print("Wynik działania " + text + " wynosi: " + str(stack.pop()))
import sys


def number(num):
    return "0" <= num <= "99999999999"


def operator(op):
    if op == "+":
        return "+"
    elif op == "-":
        return "-"
    elif op == "*":
        return "*"
    elif op == "/":
        return "/"


def dzialanie(b, a, op):
    if op == "+":
        return b + a
    elif op == "-":
        return b - a
    elif op == "*":
        return b * a
    elif op == "/":
        return b // a


stack = []
text = input("Wprowadź działanie ONP. Między liczbami i operatorami używaj znaku spacji: \n")
flag = False



########### do zrobienia


if len(stack) != 1:
    print("Nieprawidłowe wyrażenie ONP")
elif flag is False:
    print("Wynik działania " + text + " wynosi: " + str(stack.pop()))