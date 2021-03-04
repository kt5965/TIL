N = 10
arr = list(range(1, 11))
sel = [0] * N

def power(idx):
    if sel[idx] == N:
        print(sel, ':', end=' ')

        for i in range(N):
            if sel[i] != 0:
                print(arr[i], end=' ')
        print()
        return

    sel[idx] = 1
    power(idx+1)
    sel[idx] = 0
    power(idx+1)

power(0)
