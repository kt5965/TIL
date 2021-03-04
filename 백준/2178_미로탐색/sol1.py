import pandas as pd


def bfs(graph, visited):
    global a, b, N, M
    queue = [(0, 0)]
    visited.append((0, 0))
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    print(graph[N-1][M-1])






N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

for i in range(len(matrix)):
    matrix[i] = list(map(int, matrix[i]))
visited = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
a = 0
b = []
bfs(matrix, visited)