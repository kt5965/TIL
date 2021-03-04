import sys
sys.stdin = open('input.txt')


def solution(string):
    result = 1
    stack = []
    openers = ['(', '{', '[']
    closers = [')', '}', ']']

    for char in string:
        if char in openers:
            stack.append(char)

        if char in closers:
            # 닫는 괄호가 나왔는데, stack이 비어있다면(
            if not len(stack):
                result = 0
                break
            else:
                if char == ')' and stack.pop() != '(':
                    result = 0
                    break
                elif char == '}' and stack.pop() != '{':
                    result = 0
                    break
                elif char == ']' and stack.pop() != '[':
                    result = 0
                    break
    else:
        if len(stack) != 0:
            result = 0
    return result



T = int(input())
for tc in range(1, T+1):
    A = input()
    print('#{} {}'.format(tc, solution(A)))