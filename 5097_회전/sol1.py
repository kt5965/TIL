import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    a = 0
    while a < M:

        N_list.append(N_list.pop(0))
        a += 1
    print(N_list[0])
