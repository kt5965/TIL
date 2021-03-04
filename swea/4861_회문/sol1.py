import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    str_matrix = []
    for i in range(N):
        str_matrix.append(input())
        for j in range(len(str_matrix[i])-M+1):
            if str_matrix[i][j:M+j] == str_matrix[i][j:M+j][::-1]:
                result.append(str_matrix[i][j:M+j])

    matrix_row = []
    row_str = ''
    for i in range(N):
        for j in str_matrix:
            row_str += j[i]
        matrix_row.append(row_str)
        row_str =''

    for i in matrix_row:
        for j in range(len(i)-M+1):
            if i[j:M+j] == i[j:M+j][::-1]:
                result.append(i[j:M+j])

    print('#{} {}'.format(tc, result[0]))