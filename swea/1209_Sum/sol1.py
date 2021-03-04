import sys
sys.stdin = open('input.txt')
for tc in range(10):
    a = int(input())
    sum_list = []
    matrix = [list(map(int, input().split())) for _ in range(100)]
    for i in range(len(matrix)):
        sum_x = 0
        for j in range(len(matrix)):
            sum_x += matrix[i][j]
        sum_list.append(sum(matrix[i]))

    for i in range(len(matrix)):
        sum_row = 0
        for j in range(len(matrix)):
            sum_row += matrix[j][i]
        sum_list.append(sum_row)

    for i in range(len(matrix)):
        sum_cross = 0
        for j in range(len(matrix)):
            if i == j:
                sum_cross += matrix[i][j]
        sum_list.append(sum_cross)

    for i in range(len(matrix)):
        sum_cross_rev = 0
        for j in range(len(matrix)):
            if i + j == 99:
                sum_cross_rev += matrix[i][j]
        sum_list.append(sum_cross_rev)

    sum_max = 0
    for i in range(len(sum_list)):
        if sum_list[i] > sum_max:
            sum_max = sum_list[i]
    print(sum_max)