import sys
sys.stdin = open('input.txt')

def solution(A):
    stack = []
    x = 0
    result = ''
    while True:

        if x == len(A):
            for i in range(len(stack)):
                result += stack.pop()
            break

        if A[x] == '+' and len(stack) == 0:
            stack.append(A[x])
            x += 1

        elif A[x] == '*' and len(stack) == 0:
            stack.append(A[x])
            x += 1

        elif A[x] == '+' and len(stack) != 0:
            result += stack.pop()
            stack.append(A[x])
            x += 1

        elif A[x] == '*' and len(stack) != 0 and stack[-1] == '+':
            stack.append(A[x])
            x += 1

        elif A[x] == '*' and len(stack) != 0 and stack[-1] == '*':
            result += stack.pop()
            stack.append(A[x])
            x += 1

        else:
            result += A[x]
            x += 1

    x = 0
    result_sum = 0

    while True:

        if result[x] != '+' and result[x] != '*':
            stack.append(result[x])
            x += 1

        elif result[x] == '+':
            a= int(stack.pop())
            b= int(stack.pop())
            stack.append(a+b)
            x += 1

        elif result[x] == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a*b)
            x += 1

        if x == len(result):
            break

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    test_str = input()
    print('#{} {}'.format(tc, solution(test_str)))
