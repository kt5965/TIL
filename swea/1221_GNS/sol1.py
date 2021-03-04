import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    input_num = list(map(str, input().split()))
    num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    our_num = list(range(0, 10))
    for i in range(len(input_num)):
        for j in range(len(num_list)):
            if input_num[i] ==num_list[j]:
                input_num[i] = our_num[j]
    for i in range(len(input_num)-1, 0, -1):
        for j in range(i):
            if input_num[j] > input_num[j + 1]:
                input_num[j], input_num[j + 1] = input_num[j + 1], input_num[j]
    for i in range(len(input_num)):
        for j in range(len(num_list)):
            if input_num[i] ==our_num[j]:
                input_num[i] = num_list[j]
    print('#{}'.format(tc))
    print(' '.join(input_num))