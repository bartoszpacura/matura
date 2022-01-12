n = int(input(""))

a = 1
b = 1
print(a)
print()
print(b)
print()


# iteration
#
# for i in range(2, n):
#     b = a + b
#     a = b - a
#     print(b)
#     print()

# recursion
# tutaj spojrzałem do rozwiązania

def fib(m):
    if m < 3:
        return 1
    else:
        return fib(m-2)+fib(m-1)


print(fib(n))
