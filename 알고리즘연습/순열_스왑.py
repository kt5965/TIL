N = 3
arr = list(range(1, 4))
sel = [0] * N



def perm(idx):
    if idx == N:
        print(arr)


    else:
        for i in range(idx, N):
            # 순서를 바꾸고
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx + 1)
            # 원상복귀
            arr[idx], arr[i] = arr[i], arr[idx]

perm(0)
