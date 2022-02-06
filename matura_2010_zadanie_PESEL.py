pesel = []

file_pesel = open("pesel.txt")

for line in file_pesel.readlines():
    pesel.append(line.strip())

file_pesel.close()

counter_december = 0
for i in pesel:
    if i[2] == "1" and i[3] == "2":
        counter_december += 1

print("W grudniu urodziło się " + str(counter_december) + " osób")

###

counter_women = 0
for i in pesel:
    if int(i[9]) % 2 == 0:
        counter_women += 1

print()
print("W biurze pracują " + str(counter_women) + " kobiety")

###
counter_people = 0
the_most_people = 0
year = 0
year_num = 0

for i in range(99, 49, -1):
    for j in pesel:
        year = str(j[0] + j[1])
        if i == int(year):
            counter_people += 1
    if the_most_people < counter_people:
        the_most_people = counter_people
        year_num = i
        counter_people = 0
    else:
        counter_people = 0

print()
print("Najwięcej osób pracujących w biurze (" + str(the_most_people) + ") urodziło się w roku 19" + str(year_num))


###

def control_number(pesel):
    control = 0

    control += int(pesel[0])
    control += int(pesel[1]) * 3
    control += int(pesel[2]) * 7
    control += int(pesel[3]) * 9
    control += int(pesel[4])
    control += int(pesel[5]) * 3
    control += int(pesel[6]) * 7
    control += int(pesel[7]) * 9
    control += int(pesel[8])
    control += int(pesel[9]) * 3

    mod = control % 10
    if mod == 0:
        return 0
    else:
        con_num = 10 - mod
        return con_num


incorrect_number = []
counter = 1
for i in pesel:
    a = control_number(i)
    if str(a) != i[10]:
        incorrect_number.append(i)
        # print("[" + str(counter) + "] " + str(a))
    counter += 1

incorrect_number.sort()

print()
print("Nieprawidłowe numery PESEL: ")

for i in incorrect_number:
    print(i)

###

pesel.sort()

p_50 = []
p_60 = []
p_70 = []
p_80 = []
p_90 = []

for i in pesel:
    if i[0] == "5":
        p_50.append(i)
    elif i[0] == "6":
        p_60.append(i)
    elif i[0] == "7":
        p_70.append(i)
    elif i[0] == "8":
        p_80.append(i)
    elif i[0] == "9":
        p_90.append(i)

length = len(pesel)

print()
print("Liczba osób urodzonych w poszczególnych dziesięcioleciach XX wieku: ")
print("lata 50: " + str((len(p_50))))
print("lata 60: " + str((len(p_60))))
print("lata 70: " + str((len(p_70))))
print("lata 80: " + str((len(p_80))))
print("lata 90: " + str((len(p_90))))

print()
print("Procentowy rozkład liczby osób urodzonych w poszczególnych dziesięcioleciach XX wieku: ")
print("lata 50: " + str((len(p_50) / length) * 100) + " %")
print("lata 60: " + str((len(p_60) / length) * 100) + " %")
print("lata 70: " + str((len(p_70) / length) * 100) + " %")
print("lata 80: " + str((len(p_80) / length) * 100) + " %")
print("lata 90: " + str((len(p_90) / length) * 100) + " %")
