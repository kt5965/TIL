import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())
    a = list(input())
    x = 0
    stack = []
    result = ''
    while True:

        if x == len(a):
            result += stack.pop()
            break

        if a[x] == '+' and len(stack) == 0:
            stack.append(a[x])

            x += 1
        elif a[x] == '+' and len(stack) != 0:
            result += stack.pop()
            stack.append(a[x])
            x += 1

        elif a[x] != '+':
            result += a[x]
            x += 1

    x = 0
    result_sum = 0
    while True:
        if result[x] != '+':
            stack.append(result[x])
            x += 1
        elif result[x] == '+':
            result_sum += int(stack.pop())
            x += 1
        if x == len(result):
            result_sum += int(stack.pop())
            break
    print('#{} {}'.format(tc, result_sum))



