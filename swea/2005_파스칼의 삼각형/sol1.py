T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = []
    for i in range(N):
        a.append([0]*(i+1))

    for i in range(len(a)):
        a[i][0] = 1
        a[i][len(a[i])-1] = 1
    for i in range(len(a)):
        for j in range(len(a[i])):
            if len(a[i]) > 2 and 0 < j < len(a[i])-1:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
    print('#{}'.format(tc))

    for i in range(len(a)):
        a[i] = list(map(str, a[i]))

    for i in range(len(a)):
        print(' '.join(a[i]))
