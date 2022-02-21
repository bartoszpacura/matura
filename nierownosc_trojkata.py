def triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            return True
    return False


print("Podaj trzy liczby całkowite: ")
a = int(input(""))
b = int(input(""))
c = int(input(""))

if triangle(a, b, c) is True:
    print("Z podanych odcinków można zbudować trójkąt")
else:
    print("Z podanych odcinków nie można zbudować trójkąta")
