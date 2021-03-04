import sys
sys.stdin = open('input.txt')
T = int(input())

def solution(a):
    if a == 10:
        return 1
    elif a / 10 % 2 == 1:
        return solution(a-10) * 2 - 1
    else:
        return solution(a-10) * 2 + 1

for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, solution(N)))