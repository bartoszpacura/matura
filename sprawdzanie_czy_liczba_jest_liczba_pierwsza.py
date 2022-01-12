n = int(input(""))

if n > 2:
    for numbers in range(2, n):
        if n % numbers == 0:
            print("It is not prime number")
            break
        else:
            print("It is prime number")
            break
else:
    print("Invalid Value!")
