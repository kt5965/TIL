import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A_list = []
    station = [0]*5001
    for i in range(N):
        Ai, Bi = map(int, input().split())
        A_list.append(Ai)
        A_list.append(Bi)
    P = int(input())
    P_list = []
    for i in range(P):
        P_list.append(int(input()))
    d = 0
    for i in range(0, len(A_list), 2):
        d = A_list[i+1] - A_list[i]
        for j in range(A_list[i], A_list[i]+d+1):
            station[j] += 1

    for i in range(len(P_list)):
        P_list[i] = str(station[P_list[i]])
    print('#{} {}'.format(tc, ' '.join(P_list)))