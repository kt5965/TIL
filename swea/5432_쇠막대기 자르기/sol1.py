import sys
sys.stdin = open('input.txt')
T = int(input())


def cutting(bar_list):
    count = 0  # 같이 나아가는 쇠막대의 갯수
    laser = 0  # 이전이 레이저였나 판단
    result = 0  # 총 갯수
    bar = 1  # 잘리면서 두개로 나뉘므로 1 더해줘야하는 변수
    for i in range(len(bar_list)):

        # (라면 쇠막대기를 계속 늘려감 어차피 잘릴때 한번에 다 잘림
        if bar_list[i] == '(':
            count += 1
            # 레이저가 0이면 지금까지 닫히지 않고 바로 붙어있는 상태
            laser = 0
        elif bar_list[i] == ')':
            # 레이저가 0이면 닫히지 않고 (였으니 바로 오는)는 레이저를 의미
            if laser == 0:
                # 레이저 1로 바꿔줌
                laser = 1
                # 이전까지 바의 갯수 세서
                count -= 1
                # 더해줌
                result = result + count
            # 만약 이전이 레이저였다면 바꿔 줄 필요 없이 하나가 닫혔으므로 카운트 빼주고 더해줌
            elif laser == 1:
                count -= 1
                result += bar
    return result

for tc in range(1, T+1):

    bar_list = list(input())
    cutting_bar = cutting(bar_list)

    print('#{} {}'.format(tc, cutting_bar))