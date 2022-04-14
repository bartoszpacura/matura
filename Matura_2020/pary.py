# 4.1.


import math


def znajdz_liczby_pierwsze(n):
    s = int(math.sqrt(n))
    for i in range(2, s + 1):
        if n % i == 0:
            return False
    return True


file = open("pary.txt")
lines = []

save = open("wyniki_2020.txt", "a")
save.write("4.1. \n")

for i in file:
    lines.append(i.strip())

file.close()

for line in lines:
    num = int(line.split()[0])
    if num % 2 == 0:
        for n in range(2, int(num)):
            if znajdz_liczby_pierwsze(n) and znajdz_liczby_pierwsze(int(num) - n):
                print(str(num) + " " + str(n) + " " + str(num - n) + "\n")
                save.write(str(num) + " " + str(n) + " " + str(num - n) + "\n")
                break
save.close()


# 4.2.


file = open("pary.txt")

pary_tekst = []
for i in file:
    pary_tekst.append(i.split()[1])

file.close()

save = open("wyniki_2020.txt", "a")
save.write("\n4.2.\n")

for word in pary_tekst:
    tekst_max = ""
    tekst_temp = ""
    for i in range(len(word)):
        if len(tekst_temp) == 0 or tekst_temp[0] == word[i]:
            tekst_temp += word[i]
        else:
            if len(tekst_temp) > len(tekst_max):
                tekst_max = tekst_temp
            tekst_temp = ""
            tekst_temp += word[i]

    if len(tekst_temp) > len(tekst_max):
        tekst_max = tekst_temp
    print(tekst_max + " " + str(len(tekst_max)))
    save.write(tekst_max + " " + str(len(tekst_max)) + "\n")

save.close()


# 4.3.


file = open("pary.txt")

pary_temp = []
pary = []

for i in file:
    pary_temp.append(i.split())

file.close()

for n in pary_temp:
    if len(n[1]) == int(n[0]):
        pary.append(n)

minimum = pary[0]

for i in range(1, len(pary)):
    if int(pary[i][0]) < int(minimum[0]):
        minimum = pary[i]
    elif int(pary[i][0]) == int(minimum[0]):
        if pary[i][1] < minimum[1]:
            minimum = pary[i]

# wystarczyło posortować, ale nie wiem, czy by mi to zaliczyli

print("\n"+ str(minimum[0]) + " " + str(minimum[1]))

save = open("wyniki_2020.txt", "a")
save.write("\n" + "4.3. " + str(minimum[0]) + " " + str(minimum[1]))
save.close()
