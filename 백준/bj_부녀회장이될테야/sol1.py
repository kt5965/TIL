T = int(input())
for i in range(T):
    K = int(input())
    N = int(input())
    ze = [0]*N
    d = 0
    for j in range(K):
        if j == 0:
            for k in range(N):
                ze[k] = k+1
        for idx in range(1, N):
            ze[idx] = ze[idx-1] + ze[idx]
    print(ze[N-1])
