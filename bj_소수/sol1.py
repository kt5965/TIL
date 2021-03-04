def decimal():
    m = int(input())
    n = int(input())
    b = []
    for i in range(m, n+1):
        count = 0
        for j in range(2, i+1):
            if i % j == 0:
                count += 1
        if count == 1:
            b.append(i)
    if len(b) >= 1:
        min_val = b[0]
        for i in range(len(b)):
            if b[i] < min_val:
                min_val = b[i]
        x = sum(b)
        y = min_val
        return x, y
    else:
        return -1
a = decimal()
if a == -1:
    print(a)
else:
    print(a[0])
    print(a[1])