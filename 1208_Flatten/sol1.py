import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    numbers = list(map(int,input().split()))
    count = 0
    while count <= dump:
        count += 1
        max_num = 0
        min_num = 100
        a = 0
        b = 0
        for i in range(len(numbers)):
            if numbers[i] > max_num:
                max_num = numbers[i]
                a = i
            if numbers[i] < min_num:
                min_num = numbers[i]
                b = i
        if max_num - min_num == 1:
            break
        numbers[a] = numbers[a] - 1
        numbers[b] = numbers[b] + 1

    print('#{} {}'.format(tc, max_num - min_num))