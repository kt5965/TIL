import sys
sys.stdin = open('input.txt')

def solution(x, y):
    if (a[x] == 2 and a[y] == 1) or a[x] == a[y] == 2:
        return x
    elif (a[x] == 1 and a[y] == 3) or a[x] == a[y] == 1:
        return x
    elif (a[x] == 3 and a[y] == 2) or a[x] == a[y] == 3:
        return x
    else:
        return y

def binary(s, e):
    if s == e:
        return s
    left = binary(s, (s + e) // 2)
    right = binary((s + e) // 2 + 1, e)
    return solution(left, right)











T = int(input())



for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    start = 0
    end = N - 1
    print('#{} {}'.format(tc, binary(start, end)+1))
