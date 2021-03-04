import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    a = []
    b = 100
    for i in range(b):
        a.append(list(input()))
    list_pa = []
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if a[i][j:j+k] == a[i][j:j+k][::-1]:
                    list_pa.append(''.join(a[i][j:j+k]))
    for i in range(len(list_pa)):
        list_pa[i] = len(list_pa[i])
    list_pa2 = []
    x = 0

    while x < 100:
        c = ''
        for i in range(len(a)):
            c += a[i][x]
        for j in range(len(c)):
            for k in range(2, len(c) - j):
                if c[j:j + k] == c[j:j + k][::-1]:
                    list_pa2.append(''.join(c[j:j + k]))
        x += 1


    for i in range(len(list_pa2)):
        list_pa2[i] = len(list_pa2[i])


    max_a = 0
    if max(list_pa) >= max(list_pa2):
        max_a = max(list_pa)
    else:
        max_a = max(list_pa2)
    print('#{} {}'.format(tc, max_a))
