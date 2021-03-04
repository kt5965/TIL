import sys
sys.stdin = open('input.txt')
T = int(input())
d_col = [0, 1, 0, -1]
d_row = [1, 0, -1, 0]
for tc in range(T):
    N = int(input())
    a_list = [[0]*N for _ in range(N)]
    X = 0
    Y = 0
    num = 2
    d = 0
    a_list[0][0] = 1
    while num <= N**2:
        if 0 <= X+d_col[d%4] < N and 0 <= Y+d_row[d%4] < N and a_list[X+d_col[d%4]][Y+d_row[d%4]] == 0:
            X += d_col[d%4]
            Y += d_row[d%4]
            a_list[X][Y] = num
            num += 1

        else:
            d += 1
    print('#{}'.format(tc))
    for i in range(len(a_list)):
        for j in range(len(a_list[i])):
            print(a_list[i][j], end=' ')
        print()
