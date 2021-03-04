import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    p, pa, pb = map(int, input().split())
    l = 1
    r = p
    count_pa = 0
    count_pb = 0
    while l <= r:
        c = (l + r) // 2
        if c == pa:
            break
        elif c > pa:
            r = c
            count_pa += 1
        else:
            l = c
            count_pa += 1

    l = 1
    r = p
    while l <= r:
        c = (l + r) // 2
        if c == pb:
            break
        elif c > pb:
            count_pb += 1
            r = c
        else:
            count_pb += 1
            l = c
    if count_pb > count_pa:
        print('#{} A'.format(tc))
    elif count_pa > count_pb:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))


