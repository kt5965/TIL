import sys
sys.stdin = open('input.txt')



def solution(x, y, graph, visited):
    global found
    if graph[x][y] == 3:
        found = True
    visited.append((x, y))
    for i in range(4):
        if 0 <= x+ dy[i] < N and 0 <= y+dx[i] < N and graph[x+dy[i]][y+dx[i]] != 1 and (x+dy[i], y+dx[i]) not in visited:
            solution(x+dy[i], y+dx[i], graph, visited)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    found = False
    for i in range(N):
        A.append(list(input()))
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == '2':
                x = i
                y = j
                break
    visited = []
    for i in range(len(A)):
        A[i] = list(map(int, A[i]))
    solution(x, y, A, visited)
    print('#{} {}'.format(tc, found))
