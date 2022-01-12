from math import floor

r = int(input(""))

den = [200, 100, 50, 20, 10, 5, 2, 1]
history = []
count = 0

while r > 0:
    for i in range(0, len(den)):
        if r > 0:
            a = r / den[i]
            a = int(a)
            r -= (den[i] * a)
            if a > 0:
                count += 1
                history.append(den[i])
                print(str(a) + " x " + str(den[i]) + " zł")
        else:
            break

print("Resztę można wydać " + str(count) + " nominałami")

# Muszę jeszcze pomyśleć, w jaki sposób dodać pozostałe monety

