N = int(input())
a = []
for i in range(N):
    a.append(tuple(map(int,input().split())))
for i in a:
    rank = 1
    for j in a:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")