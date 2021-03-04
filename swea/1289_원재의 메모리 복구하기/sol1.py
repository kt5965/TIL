import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    A = input()
    count = 0
    result = 0
    for i in A:
        if count == 0 and i == '1':
            count += 1
            result += 1
        if i == '0' and count == 1:
            count = 0
            result += 1

    print('#{} {}'.format(tc, result))
