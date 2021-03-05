import sys
sys.stdin = open('input.txt')

def solution(graph, L):
    max_h = 0
    # 부분집합
    for i in range(1 << len(graph)):
        a = []
        for j in range(len(graph)):
            if i & (1 << j):
                a.append(graph[j])

        hc = []
        # 그 안에서 칼로리와 행복지수
        happy = 0
        cal = 0
        for i in range(len(a)):
            happy += a[i][0]
            cal += a[i][1]
            hc.append((happy, cal))

        # 칼로리 내에서 가장 행복한거
        for i in range(len(hc)):
            if hc[i][1] <= L:
                if max_h < hc[i][0]:
                    max_h = hc[i][0]
        print(a)

    return max_h

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    q = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, solution(q, L)))