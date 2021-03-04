
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 나무의 가격, 심을 위치등을 2차원 리스트로 받아옴
    tree = []
    for i in range(N):
        tree.append(list(map(int, input().split())))

    # 심어지는 나무의 위치에 따른 가격을 price 라는 변수에 더함
    # tree_price 는 심어지는 나무의 가격을 각각 저장해줌
    price = 0
    tree_price = []
    for i in range(0, len(tree[0]), 2):
        for j in range(0, N):
            # i먼저 돌리며 i는 열을 의미하므로 2칸씩 건너 뛰어가며 더함
            price += tree[j][i]
            tree_price.append(tree[j][i])

    # 가장 큰 가격을 갖는 나무가 뽑아온 나무들 중 몇번째 위치에 있는지 판단
    # 만약 뒤에 같은 가격이 심어지면 그걸 선택
    max_price = 0
    max_idx = 0
    for i in range(len(tree_price)):
        if tree_price[i] >= max_price:
            max_price = tree_price[i]
            max_idx = i

    # max_idx를 행의 갯수로 나눠준 몫을 구하고 2를 곱해준 후 1을 더하면 몇번째 열에 있는지 알 수 있음.
    # ex) 3*5 행렬에서 max_idx가 5열에 있다면 앞에 나무가 채워진 열은 1, 3 두 개 이다.
    # 5열의 나무 값들은 6번째 숫자부터 들어가므로 6//3 = 2 이고 2*2+1 = 5가 나온다.
    # 5열의 6, 7, 8 idx는 전부 같은 값이 나온다.

    print('#{} {} {} {} {}'.format(tc, price, len(tree_price), max_price, max_idx//N * 2 + 1))
