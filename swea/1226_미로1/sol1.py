import sys
sys.stdin = open('input.txt')

def bfs(graph):
    global ans
    queue = [(1, 1)]
    visited = [(1, 1)]

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < 16 and 0<= ny < 16 and graph[nx][ny] != 1 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.append((nx, ny))
                if graph[nx][ny] == 3:
                    ans = 1

for tc in range(1, 11):
    a = int(input())
    b = [list(input()) for _ in range(16)]
    for i in range(len(b)):
        b[i] = list(map(int, b[i]))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 0
    bfs(b)
    print('#{} {}'.format(tc, ans))