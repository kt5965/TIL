import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [[0]*N for _ in range(N)]
    for i in range(N):
        a = input()
        for j in range(N):
            farm[i][j] = int(a[j])

    result = 0
    x = 0
    y = 0
    while True:
        if x == N:
            break

        if N//2 >= x:
            for i in range(N//2-x, N//2+x+1):
                result += farm[x][i]
        elif N//2 < x:
            for i in range(x-N//2, N//2*3-x+1):
                result += farm[x][i]
        x += 1

    print('#{} {}'.format(tc, result))
