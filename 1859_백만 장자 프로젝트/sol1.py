import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    count = 0
    num = 0
    x = numbers[-1]

    for i in range(len(numbers)-1, -1, -1):
        if x > numbers[i]:
            count = count + x - numbers[i]
        else:
            x = numbers[i]
    print('#{} {}'.format(tc, count))


