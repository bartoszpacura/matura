numbers = []


def fun_1(num_1, base):
    if num_1 == 0:
        return num_1 % base
    else:
        mod = num_1 % base
        div = (num_1 - mod) / base
        print(mod)

        if 0 <= mod < 10:
            numbers.append(int(mod))

        if mod == 10:
            numbers.append("A")

        if mod == 11:
            numbers.append("B")

        if mod == 12:
            numbers.append("C")

        if mod == 13:
            numbers.append("D")

        if mod == 14:
            numbers.append("E")

        if mod == 15:
            numbers.append("F")

        return fun_1(div, base)


n = int(input(""))
p = int(input(""))

if 1 < p < 17:
    fun_1(n, p)
else:
    "Invalid value!"

numbers.reverse()
print(numbers)