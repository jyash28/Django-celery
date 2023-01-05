a = [2, 3, 1, 4, -2, -4, 0]
b = []
for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
b.extend(a)
print(b)

