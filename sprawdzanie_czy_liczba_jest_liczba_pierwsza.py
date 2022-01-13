from math import sqrt

n = int(input(""))
m = False

if n < 2:
    print("It is not prime number")
    exit()

elif n > 2:
    for numbers in range(2, n):
        if n % numbers == 0:
            m = True
            break

if m is True:
    print("It is not prime number")
elif m is False:
    print("It is prime number")
