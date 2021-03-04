a = [1, 3, 5, 7]
for i in range(1 << len(a)):
    for j in range(len(a)):
        if i & (1 << j):
            print(i, j)
    print()