import sys
sys.stdin = open('input.txt')


def solution(N, matrix, start, goal):

    def dfs(x, y):
        if matrix[y][x] == 3:
            print('찾았다')
        else:
            dys = [-1, 1, 0, 0]
            dxs = [0, 0, -1, 1]
            for idx in range(4):
                dy, dx = dys[idx], dxs[idx]
                if 0 <= x + dx < N and 0 <= y + dy < N:
                    if matrix[y + dy][x + dx] == 0 or matrix[y +dy][x + dx] == 2 or matrix[y + dy][x + dx] == 3:
                        pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 2:
                start = (x, y)
            elif matrix[y][x] == 3:
                goal = (x, y)

    print('#{} {}'.format(tc, solution(N, matrix, start, goal)))