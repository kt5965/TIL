N = 3
arr = list(range(1, 4))
sel = [0] * N
check = [0] * N


def perm(idx):
    if idx == N:
        print(sel)


    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i] #값을 써라
                check[i] = 1 # 사용했다는 표시
                perm(idx+1)
                check[i] = 0 # 다음 반복문을 위한 원상복구

perm(0)