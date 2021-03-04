import sys
sys.stdin = open('input.txt')

def solution(A):
    stack = []
    x = 0
    while True:


        if A[x] == '.':
            if len(stack) != 1:
                return 'error'
            else:
                break
        if A[x] != '+' and A[x] != '*' and A[x] != '/' and A[x] != '-':
            stack.append(A[x])
            x += 1

        elif A[x] == '+':
            if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b + a)
                x += 1
            else:
                return 'error'

        elif A[x] == '*':
            if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b * a)
                x += 1
            else:
                return 'error'

        elif A[x] == '/':
            if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b / a)
                x += 1
            else:
                return 'error'

        elif A[x] == '-':
            if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
                x += 1
            else:
                return 'error'
    return int(sum(stack))

T = int(input())
for tc in range(1, T+1):
    test_str = input().split()
    print('#{} {}'.format(tc, solution(test_str)))