# 4.1.

# file = open("slowa.txt")
#
# counter = 0
# for word in file:
#     counter_zero = 0
#     counter_one = 0
#     for i in word:
#         if i == "0":
#             counter_zero += 1
#         elif i == "1":
#             counter_one += 1
#     if counter_zero > counter_one:
#         counter += 1
#
# print(counter)


# 4.2.


# file = open("slowa.txt")
# words = []
#
# for i in file:
#     words.append(i.strip())
#
# counter = 0
# for word in words:
#     counter_changes = 0
#     if word[0] != "0":
#         continue
#     else:
#         for i in range(len(word) - 1):
#             if word[i] != word[i + 1]:
#                 counter_changes += 1
#         if counter_changes == 1:
#             counter += 1
#
# print(counter)


# 4.3.


file = open("slowa.txt")

words = []

for i in file:
    words.append(i.strip())

counter_max = 0
for word in words:
    counter_max_temp = 0
    for i in range(len(word)):
        if word[i] == "0":
            counter_max_temp += 1
        else:
            if counter_max_temp > counter_max:
                counter_max = counter_max_temp
            counter_max_temp = 0

for word in words:
    if "0000000000" in word:
        print(word)
