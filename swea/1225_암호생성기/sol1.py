import sys
sys.stdin = open('input.txt')

def solution(a):
    c = 0
    while a[-1] > 0:
        c += 1
        if c == 6:
            c = 1
        b = a.pop(0)
        a.append(b - c)
    a[-1] = 0
    return a

for tc in range(1, 11):
    t = int(input())
    a = list(map(int, input().split()))
    solution(a)
    a = map(str, a)
    print('#{} {}'.format(tc, ' '.join(a)))
