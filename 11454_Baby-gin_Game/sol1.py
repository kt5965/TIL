import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input()))
    counter = [0] * 10
    # 2가 되면 성공
    is_babygin = 0

    for card in cards:
        counter[card] += 1

    for idx in range(len(counter)):
        if counter[idx] >= 3:
            is_babygin += 1
            counter[idx] -= 3

        if idx < 8:

            if counter[idx] and counter[idx+1] and counter[idx+2]:
                is_babygin += 1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
    if is_babygin == 2:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))