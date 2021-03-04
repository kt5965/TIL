import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    numbers = list(map(int, input().split()))
    count = 0
    for i in range(2, len(numbers)-2):
        a = 0
        b = 0
        c = 0
        d = 0
        if numbers[i] > numbers[i+1] and numbers[i] > numbers[i+2] and numbers[i] > numbers[i-1] and numbers[i] > numbers[i-2]:
            a = abs(numbers[i+2] - numbers[i])
            b = abs(numbers[i+1] - numbers[i])
            c = abs(numbers[i-2] - numbers[i])
            d = abs(numbers[i-1] - numbers[i])
            if a <= b and a <= c and a <= d:
                count += a
            elif b <= a and b <= c and b <= d:
                count += b
            elif c <= a and c <= b and c <= d:
                count += c
            elif d <= a and d <= b and d <= c:
                count += d
    print('#{} {}'.format(tc, count))