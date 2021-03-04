import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    length_str, test_str = map(str, input().split())
    stack = []
    x = 0
    count = 0
    while True:
        if test_str[x] == test_str[x+1]:
            if len(test_str) > x+2:
                stack.append(test_str[0:x]+test_str[x+2:])
                x = 0
            else:
                stack.append(test_str[0:x])
                x = 0

            test_str = stack.pop()
            count = 0

            if len(test_str) == 1:
                break
        else:
            x += 1
        count += 1
        if count == len(test_str):
            break
    print('#{} {}'.format(tc, test_str))