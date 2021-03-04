import sys
sys.stdin = open('input.txt')
T = int(input())

def solution(sd):

    for i in range(9):
        if len(set(sd[i])) != 9:
            return 0

    for i in range(9):
        a = []
        for j in range(9):
            a.append(sd[j][i])
        if len(set(a)) != 9:
            return 0

    for i in range(0,9,3):
        for j in range(0,9,3):
            b = []
            for k in range(3):
                for l in range(3):
                    b.append(sd[i+k][j+l])
            if len(set(b)) != 9:
                return 0

    return 1

for tc in range(1, T+1):
    sd = []

    for i in range(9):
        sd.append(list(map(int,input().split())))

    print('#{} {}'.format(tc, solution(sd)))
