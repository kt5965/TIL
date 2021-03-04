import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = []
    for i in range(N):
        s.append(list(map(int, input().split())))

    s90 = [[]*len(s) for i in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s[i])-1, -1, -1):
            s90[i].append(s[j][i])

    s180 = [[]*len(s) for i in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s[i])-1, -1, -1):
            s180[i].append(s90[j][i])

    s270 = [[]*len(s) for i in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s[i])-1, -1, -1):
             s270[i].append(s180[j][i])
    print('#{}'.format(tc))
    for i in range(len(s)):
        for j in range(len(s[i])):
            print(s90[i][j], end='')
        print(' ', end='')
        for j in range(len(s[i])):
            print(s180[i][j], end='')
        print(' ', end='')
        for j in range(len(s[i])):
            print(s270[i][j], end='')
        print(' ', end='')
        print()
