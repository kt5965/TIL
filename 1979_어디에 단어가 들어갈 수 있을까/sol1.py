import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
    result = 0
    for i in range(len(puzzle)):
        puzzle_one = 0
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 1:
                puzzle_one += 1
                if puzzle_one == K:
                    result += 1
            elif puzzle[i][j] == 0:
                puzzle_one = 0

            if puzzle_one == K+1:
                puzzle_one = 0
                result -= 1

    for i in range(len(puzzle)):
        puzzle_one = 0
        for j in range(len(puzzle[i])):
            if puzzle[j][i] == 1:
                puzzle_one += 1
                if puzzle_one == K:
                    result += 1
            elif puzzle[j][i] == 0:
                puzzle_one = 0

            if puzzle_one == K+1:
                puzzle_one = 0
                result -= 1


    print('#{} {}'.format(tc, result))
