import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    coordinate = [[0]*10 for _ in range(10)]
    for i in range(N):
        square_list = list(map(int, input().split()))
        if square_list[4] == 1:
            for i in range(square_list[0], square_list[2] + 1):
                for j in range(square_list[1], square_list[3] + 1):
                    coordinate[i][j] += 1
        elif square_list[4] == 2:
            for i in range(square_list[0], square_list[2] + 1):
                for j in range(square_list[1], square_list[3] + 1):
                    coordinate[i][j] += 1
    result = 0
    for i in range(10):
        for j in range(10):
            if coordinate[i][j] == 2:
                result += 1
    print('#{} {}'.format(tc, result))

