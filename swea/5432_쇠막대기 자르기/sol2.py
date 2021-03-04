# test_case 갯수
T = int(input())

for test_case in range(1,T+1):
    # 레이저 위치를 r로 replace
    data = input()
    data = data.replace('()', 'r')
    bar = 0

    # 나눠지는 막대기 갯수 구하기
    for s_idx, start in enumerate(data):
        e_idx = 0
        count = 0
        # 만약 막대기의 시작점('(')이라면
        if start == '(':
            # 시작점부터 data의 마지막까지
            for j in range(s_idx,len(data)):
                # '('의 갯수와 ')'의 갯수를 비교해 막대기의 종료점 index (e_idx)를 찾는다.
                if data[j] == '(':
                    count += 1
                elif data[j] == ')':
                    count -= 1
                    if count == 0:
                        e_idx = j
                        break
            # 막대기는 막대기의 시작과 종료 사이에 존재하는 레이저의 갯수 + 1개로 나누어진다.
            bar += data[s_idx:e_idx].count('r') + 1

    # 출력
    print('#{} {}'.format(test_case, bar))