import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    for i in range(len(ai)):
        max_ai = i
        min_ai = i
        if i % 2 == 0:
            for j in range(i, len(ai)):
                if ai[max_ai] < ai[j]:
                    max_ai = j
            ai[i], ai[max_ai] = ai[max_ai], ai[i]
        if i % 2 == 1:
            for j in range(i, len(ai)):
                if ai[min_ai] > ai[j]:
                    min_ai = j
            ai[i], ai[min_ai] = ai[min_ai], ai[i]
    str_list = []
    for i in range(10):
        str_list.append(str(ai[i]))

    print('#{} {}'.format(tc, ' '.join(str_list)))