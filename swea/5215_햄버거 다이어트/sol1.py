import sys
sys.stdin = open('input.txt')

def solution(graph, L):
    a = [[] for _ in range(2**len(graph))]
    # 부분집합
    for i in range(1 << len(graph)):
        for j in range(len(graph)):
            if i & (1 << j):
                a[i].append(graph[j])
        print(a[i])
    max_h = 0
    # 그 안에서 칼로리와 행복지수
    for i in range(len(a)):
        happy = 0
        cal = 0
        for j in range(len(a[i])):
            happy += a[i][j][0]
            cal += a[i][j][1]
        if cal <= L:
            if max_h <= happy:
                max_h = happy

    return max_h

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    q = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, solution(q, L)))