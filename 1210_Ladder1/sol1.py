import sys
sys.stdin = open('input (1).txt')
for tc in range(1, 11):
    N = int(input())
    ladder = []
    x = 99
    y = 0
    for i in range(100):
        l = list(map(int, input().split()))
        ladder.append(l)
    for i in range(100):
        if ladder[x][i] == 2:
            y = i

    while True:
        if y < 99 and ladder[x][y+1] == 1:
            while y < 99 and ladder[x][y+1] == 1:
                y += 1
            x -= 1
        elif 0 <= y and ladder[x][y-1] == 1:
            while 0 <= y and ladder[x][y-1] == 1:
                y -= 1
            x -= 1
        else:
            x -= 1
        if x == 0:
            break
    print('#{} {}'.format(tc, y))

