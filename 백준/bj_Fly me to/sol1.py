A = int(input())
for i in range(A):
    B, C = map(int,input().split())
    dist = C - B
    num = 1
    while True:
        if num**2 - num + 1 <= dist <= num**2:
            print(2*num-1)
            break
        elif num**2 + 1 <= dist <= num**2 + num:
            print(2*num)
            break
        num += 1