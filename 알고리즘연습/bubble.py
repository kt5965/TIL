a = [7, 5, 8, 3, 1]
print(a)
for i in range(len(a)-1, 0, -1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(i, j, a)