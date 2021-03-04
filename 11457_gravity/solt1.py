import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    number = int(input())
    number_list = list(map(int, input().split()))
    count_list = []
    for i in range(len(number_list)):
        count = 0
        for j in range(i, len(number_list)):
            if number_list[j] == 0 and number_list[i] != 0:
                count += 1
        count_list.append(count)
    for i in range(len(number_list)):
        for j in range(i, len(number_list)):
            if number_list[i] > number_list[j] and number_list[j] != 0:
                count_list[i] += 1
    print('#{} {}'.format(tc, max(count_list)))