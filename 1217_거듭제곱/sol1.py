def solution(x, y):
    if y == 0:
        return 1

    # 계산을 한 번만 하기 위해서 변수에 저장
    semi_result = solution(x, y // 2)

    # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
    if y % 2 == 0:
        return semi_result * semi_result
    else:
        return x * semi_result * semi_result

for tc in range(1, 11):
    T = input()
    a, b = map(int,input().split())
    print('#{} {}'.format(tc, solution(a, b)))