import sys
sys.stdin = open('input.txt')
T = int(input())

def solution(A, visited):
    global sum_A, x, result
    if result < sum_A:
        return result
    if x == N:
        if sum_A < result:
            result = sum_A
        return result


    for i in range(N):
        if not visited[i]:
            visited[i] = True
            sum_A += A[x][i]
            x += 1
            solution(A, visited)
            x -= 1
            visited[i] = False
            sum_A -= A[x][i]
    return result


for tc in range(1, T+1):
    N = int(input())
    A = []
    visited = [False]*N
    sum_A = 0
    x = 0
    result = 99999999
    for i in range(N):
        A.append(list(map(int,input().split())))
    print('#{} {}'.format(tc, solution(A, visited)))

