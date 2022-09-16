s = 0
for j in range(0, 40):
    if j % 5 == 0:
        s = s + j
print(s)
for k in range(1, 5, 2):
    print(k ** 2, end='')
print("")
a = 0
i = 1
while i <= 10:
    if i >= 4:
        break
    a = a + i
    i = i + 1
    print(a, end='')