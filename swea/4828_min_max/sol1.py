import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(N)
    max_i = ai[0]
    min_i = ai[0]
    result = 0
    for i in range(N):
        if min_i > ai[i]:
            min_i = ai[i]
        if max_i < ai[i]:
            max_i = ai[i]
    result = max_i - min_i
    print('#{} {}'.format(tc, result))
