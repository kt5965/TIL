
T = int(input())
for tc in range(1, T+1):
    # 누가먼저 할까 받아줌
    who = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # count_a, b는 각각 A와 B의 위치를 나타냄.
    count_a = 0
    count_b = 0

    # idx는 몇 번째 주사위인지 나타냄
    count_a_idx = 0
    count_b_idx = 0

    # 10번 돌리는 변수
    count = 0

    # 이긴 사람
    win =''

    # 만약 A가 선이면 count_a부터 값을 더해주고 20이상이 되면 나와줌
    if who == 'A':
        while count < 10:
            count_a += A[count_a_idx]
            if count_a >= 20:
                win = 'A'
                break
            # 만약 a와 b의 위치가 같다면 b가 잡아먹힘
            if count_a == count_b:
                count_b = 0

            # b도 주사위 굴림
            count_b += B[count_b_idx]
            if count_b >= 20:
                win = 'B'
                break
            # 만약 b와 a의 위치가 같다면 a가 잡아먹힘
            if count_b == count_a:
                count_a = 0
            count_a_idx += 1
            count_b_idx += 1
            count += 1

    # B가 선일경우 반대로 B먼저 굴림
    elif who == 'B':
        while count < 10:
            count_b += B[count_b_idx]
            if count_b >= 20:
                win = 'B'
                break
            if count_b == count_a:
                count_a = 0

            count_a += A[count_a_idx]
            if count_a >= 20:
                win = 'A'
                break
            if count_a == count_b:
                count_b = 0

            count_a_idx += 1
            count_b_idx += 1
            count += 1

    # 승자가 없다면 'AB'를 아니라면 승자를 출력
    if win == '':
        print('#{} {}'.format(tc, 'AB'))
    else:
        print('#{} {}'.format(tc, win))