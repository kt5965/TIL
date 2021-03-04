import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    d = []
    for i in range(len(c)-b+1):
        e = 0
        for j in range(b):
            e += c[i+j]
        d.append(e)
    max_d = d[0]
    min_d = d[0]
    for i in range(len(d)):
        if max_d < d[i]:
            max_d = d[i]
        if min_d > d[i]:
            min_d = d[i]
    print('#{} {}'.format(tc, max_d-min_d))