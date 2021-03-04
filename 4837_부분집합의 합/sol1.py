import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    count = 0
    for i in range(1<<12):
        number_list = []
        for j in range(12):
            if i & (1 << j):
                number_list.append(number[j])

        sum_list = 0
        for i in range(len(number_list)):
            sum_list += number_list[i]
        if len(number_list) == N and sum_list == K:
            count += 1
    print("#{} {}".format(tc, count))