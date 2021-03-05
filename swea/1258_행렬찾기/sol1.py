import sys
sys.stdin = open('input.txt')

def solution(matrix):
    c = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            a = 1
            b = 0
            if matrix[i][j] != 0:
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop(0)
                    matrix[x][y] = 0
                    for k in range(2):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 0 and dx[k] == 1:
                            queue.append((nx, ny))
                            matrix[nx][ny] = 0
                            a += 1
                        elif 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 0 and dy[k] == 1:
                            queue.append((nx, ny))
                            matrix[nx][ny] = 0
                            b += 1
                c.append((a, b//a+1))


    for i in range(len(c) - 1, 0, -1):
        for j in range(i):
            if c[j][0] * c[j][1] > c[j+1][0] * c[j+1][1]:
                c[j], c[j + 1] = c[j + 1], c[j]
            elif c[j][0] * c[j][1] == c[j+1][0] * c[j+1][1]:
                if c[j][0] > c[j][1]:
                    c[j], c[j + 1] = c[j + 1], c[j]


    print(len(c), end=' ')
    for i in c:
        print(i[0], i[1], end=' ')




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0]
    dy = [0, 1]
    print('#{}'.format(tc), end=' ')
    solution(matrix)
    print()