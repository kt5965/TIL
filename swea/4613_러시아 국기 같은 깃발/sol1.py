import sys
sys.stdin = open('input.txt')
T = int(input())





def sol(matrix):
    a = 1
    b = len(matrix) - 1
    d = []
    while True:
        count = 0
        for i in range(a):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 'W':
                    count += 1

        for i in range(a, b):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 'B':
                    count += 1

        for i in range(b, len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 'R':
                    count += 1

        d.append(count)
        b -= 1
        if b == a:
            a += 1
            b = len(matrix) -1
        if a == len(matrix) -1:
            break
    return min(d)

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    sol(matrix)
    print('#{} {}'.format(tc, sol(matrix)))

