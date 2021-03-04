import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    list_station = [0]*N
    copy_list = list(list_station)
    a = 0
    count = 0
    for number in numbers:
        copy_list[int(number)] += 1
    for i in range(len(copy_list)-K+1):
        if i < len(copy_list) - K:
            for j in range(K, 0, -1):
                if copy_list[i+j] == 1 and i >= a:
                    if a+K < N and a < i+j:
                        a = i+j
                        count += 1
    for i in range(len(numbers)-1):
        if K < (numbers[i+1] - numbers[i]):
            print('#{} {}'.format(tc, 0))
            break
    else:
        print('#{} {}'.format(tc, count))
