import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    count = 0
    x = 0
    while True:
        if A[x:x+len(B)] == B:
            count += 1
            if x+len(B) == len(A):
                break
            x = x+len(B)
        else:
            x += 1
            count += 1
        if x == len(A):
            break
    print('#{} {}'.format(tc, count))
