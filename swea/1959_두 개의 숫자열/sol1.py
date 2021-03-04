import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bi = list(map(int, input().split()))
    max_num = 0
    if N < M:
        for i in range(0, M-N+1):
            result = 0
            for j in range(0, N):
                result += Ai[j] * Bi[i+j]
            if result > max_num:
                max_num = result
    else:
        for i in range(0, N-M+1):
            result = 0
            for j in range(0, M):
                result += Ai[i+j] * Bi[j]
            if result > max_num:
                max_num = result
    print('#{} {}'.format(tc,max_num))