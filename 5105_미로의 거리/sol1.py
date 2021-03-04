import sys
sys.stdin = open('input.txt')

def bfs(matrix, x, y):
    global ans
    queue = []
    queue.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 1 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                if matrix[nx][ny] == 3:
                    ans = dist[nx][ny]-1
                    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    for i in range(len(matrix)):
        matrix[i] = list(map(int, matrix[i]))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 2:
                x = i
                y = j
                break
    visited = []
    ans = 0
    dist = [[0]*N for _ in range(N+1)]
    bfs(matrix, x, y)
    print('#{} {}'.format(tc, ans))