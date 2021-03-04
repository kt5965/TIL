import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = input()
    ai = input()
    ai_list = list(ai)
    list_a = [0]*10
    list_b = []
    for i in ai_list:
        list_a[int(i)] += 1
    count_max = list_a[0]
    max_number = 0
    for i in range(len(list_a)):
        if count_max <= list_a[i]:
            count_max = list_a[i]
            max_number = i
    print('#{} {} {}'.format(tc, max_number, list_a[max_number]))
