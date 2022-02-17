def sort(studenci):
    studenci.sort()

    for i in range(len(studenci)):
        for j in range(len(studenci)):
            if studenci[i][0] == studenci[j][0]:
                if studenci[i][1] > studenci[j][1]:
                    studenci[i], studenci[j] = studenci[j], studenci[i]

    return studenci


studenci = [
    ("Kowalski",  3.12),
    ("Kasprowicz",  4.40),
    ("Nowak",    6.00),
    ("Kosak",    5.44),
    ("Nasiadka",  5.32),
    ("Nowicki",    3.44),
    ("Kanigowski",  4.00),
    ("Danusiak",  4.00),
    ("Dworznik",  4.20),
    ("Kaspro",    3.00),
    ("Kasprowicz",  4.00),
    ("Kasprowicz",  3.10),
    ("Danusiak",  2.00),
    ("Danusiak",  2.14)
]

print("Dane studentów przed posortowaniem: ")
for i in range(len(studenci)):
    print(studenci[i])

sorted_s = sort(studenci)

print()
print("Dane studentów po posortowaniu: ")
for i in range(len(sorted_s)):
    print(sorted_s[i])
