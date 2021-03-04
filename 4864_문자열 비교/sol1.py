import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    first_str = input()
    second_str = input()
    count = 0
    if first_str in second_str:
        count += 1
    print('#{} {}'.format(tc, count))
