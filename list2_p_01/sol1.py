import sys

sys.stdin = open("input.txt")

T = int(input())
d_row = [0, 0, -1, 1]
d_col = [-1, 1, 0, 0]
for tc in range(1, T + 1):
    a = int(input())
    a_list = []
    for i in range(a):
        numbers = list(map(int,input().split()))
        a_list.append(numbers)
    sum_result = 0
    for i in range(len(a_list)):
        for j in range(len(a_list[i])):
            result = 0
            for k in range(4):
                X = i + d_row[k]
                Y = j + d_col[k]
                if 0 <= X < len(a_list) and 0 <= Y < len(a_list):
                    dif = a_list[i][j] - a_list[X][Y]
                    if dif >= 0:
                        dif = dif
                    else:
                        dif = -dif
                    result += dif
            sum_result += result
    print(sum_result)



