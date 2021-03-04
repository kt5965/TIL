import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    customer = list(map(int, input().split()))
    fish = [0] * 11112

    y = M
    a = 0
    while True:
        if y == len(fish):
            break
        if y % M == 0:
            a += K
        fish[y] += a
        y += 1



    x = 0
    result = 'Possible'
    while True:
        if x == len(customer):
            break
        for i in range(customer[x], len(fish)):
            fish[i] -= 1
            if fish[i] == -1:
                result = 'Impossible'
                break
        if result == 'Impossible':
            break
        x += 1
    print('#{} {}'.format(tc, result))