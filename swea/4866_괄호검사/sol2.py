T = int(input())
for tc in range(1, T+1):
    A = input()
    result = 1
    opener = ['(', '{']
    closer = [')', '}']
    stack = []
    for idx in A:
        if idx in opener:
            stack.append(idx)

        if idx in closer:

            if len(stack) == 0:
                result = 0
                break
            else:
                if idx == ')' and stack.pop() != '(':
                    result = 0
                    break
                elif idx == '}' and stack.pop() != '{':
                    result = 0
                    break

    else:
        if len(stack) != 0:
            result = 0
    print('#{} {}'.format(tc, result))