import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N // 2 - 1][N // 2- 1] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2 ][N // 2 - 1] = 1
    board[N // 2][N // 2] = 2

    for i in range(M):
        A, B, C = map(int, input().split())
        board[A-1][B-1] = C
        x = 1
        y = 1
        a = []
        while True:
            if A-1-x == -1:
                break

            if board[A-1-x][B-1] != C and board[A-1-x][B-1] != 0:
                a.append(A-1-x)
                x += 1

            elif board[A-1-x][B-1] == 0:
                a = []
                x += 1
                break

            elif board[A-1-x][B-1] == C:
                for j in range(len(a)):
                    board[a[j]][B-1] = C
                x += 1
                break


        x = 1
        y = 1
        a = []
        while True:
            if A-1+x == N:
                break

            if board[A-1+x][B-1] != C and board[A-1+x][B-1] != 0:
                a.append(A-1+x)
                x += 1
            elif board[A-1+x][B-1] == 0:
                a = []
                x += 1
                break
            elif board[A-1+x][B-1] == C:
                for j in range(len(a)):
                    board[a[j]][B-1] = C
                break

        x = 1
        y = 1
        a = []
        while True:
            if B - 1 + y == N:
                break

            if board[A - 1][B - 1 + y] != C and board[A - 1][B - 1 + y] != 0:
                a.append(B - 1 + y)
                y += 1
            elif board[A - 1][B - 1 + y] == 0:
                a = []
                y += 1
                break
            elif board[A - 1][B - 1 + y] == C:
                for j in range(len(a)):

                    board[A - 1][a[j]] = C
                break


        x = 1
        y = 1
        a = []
        b = []
        while True:
            if B - 1 - y == -1:
                break

            if board[A - 1][B - 1 - y] != C and board[A - 1][B - 1 - y] != 0:
                a.append(B - 1 - y)
                y += 1
            elif board[A - 1][B - 1 - y] == 0:
                a = []
                y += 1
                break
            elif board[A - 1][B - 1 - y] == C:
                for j in range(len(a)):
                    board[A - 1][a[j]] = C
                break


        x = 1
        y = 1
        a = []
        b = []
        while True:
            if B - 1 + y == N or A-1+x == N:
                break

            if board[A - 1 + x][B - 1 + y] != C and board[A - 1 + x][B - 1 + y] != 0:
                a.append(A - 1 + x)
                b.append(B - 1 + y)
                x += 1
                y += 1
            elif board[A - 1 + x][B - 1 + y] == 0:
                break
            elif board[A - 1 + x][B - 1 + y] == C:
                for j in range(len(a)):
                    board[a[j]][b[j]] = C
                break

        x = 1
        y = 1
        a = []
        b = []
        while True:
            if B - 1 - y == -1 or A - 1 + x == N:
                break

            if board[A - 1 + x][B - 1 - y] != C and board[A - 1 + x][B - 1 - y] != 0:
                a.append(A - 1 + x)
                b.append(B - 1 - y)
                x += 1
                y += 1
            elif board[A - 1 + x][B - 1 - y] == 0:
                break
            elif board[A - 1 + x][B - 1 - y] == C:
                for j in range(len(a)):
                    board[a[j]][b[j]] = C
                break

        x = 1
        y = 1
        a = []
        b = []
        while True:
            if B - 1 - y == -1 or A - 1 - x == -1:
                break

            if board[A - 1 - x][B - 1 - y] != C and board[A - 1 - x][B - 1 - y] != 0:
                a.append(A - 1 - x)
                b.append(B - 1 - y)
                x += 1
                y += 1
            elif board[A - 1 - x][B - 1 - y] == 0:
                break
            elif board[A - 1 - x][B - 1 - y] == C:
                for j in range(len(a)):
                    board[a[j]][b[j]] = C
                break

        x = 1
        y = 1
        a = []
        b = []
        while True:
            if B - 1 + y == N or A - 1 - x == -1:
                break

            if board[A - 1 - x][B - 1 + y] != C and board[A - 1 - x][B - 1 + y] != 0:
                a.append(A - 1 - x)
                b.append(B - 1 + y)
                x += 1
                y += 1
            elif board[A - 1 - x][B - 1 + y] == 0:
                break
            elif board[A - 1 - x][B - 1 + y] == C:
                for j in range(len(a)):
                    board[a[j]][b[j]] = C
                break

    count_black = 0
    count_white = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 2:
                count_white += 1

            elif board[i][j] == 1:
                count_black +=1
    print('#{} {} {}'.format(tc, count_black, count_white))


