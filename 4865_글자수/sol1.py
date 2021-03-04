import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    first_str = input()
    second_str = input()
    count = [0] * len(first_str)
    for i in range(len(first_str)):
        for j in range(len(second_str)):
            if first_str[i] == second_str[j]:
                count[i] += 1
    max_count = 0
    for i in range(len(count)):
        if max_count < count[i]:
            max_count = count[i]
    print('#{} {}'.format(tc, max(count)))