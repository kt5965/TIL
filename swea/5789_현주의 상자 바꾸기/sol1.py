import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    list_N = [0]*N
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            list_N[j] = i+1
    for i in range(len(list_N)):
        list_N[i] = str(list_N[i])
    print('#{} {}'.format(tc+1, ' '.join(list_N)))