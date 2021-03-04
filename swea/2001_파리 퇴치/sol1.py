import sys
sys.stdin = open('input (1).txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    coordinate = []
    for i in range(N):
        coordinate.append(list(map(int, input().split())))
    print(coordinate)
    die_list = []
    for k in range(0, N-M+1):
        for f in range(0, N-M+1):
            die_fly = 0
            for i in range(k, k+M):
                for j in range(f, f+M):
                    die_fly += coordinate[i][j]
            die_list.append(die_fly)
    max_die = 0
    for i in range(len(die_list)):
        if max_die < die_list[i]:
            max_die = die_list[i]

    print('#{} {}'.format(tc, max_die))
