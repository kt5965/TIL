import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(len(A)-1, 0, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    A = map(str,A)
    print('#{} {}'.format(tc,' '.join(A)))