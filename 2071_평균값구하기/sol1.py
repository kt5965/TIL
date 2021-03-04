import sys
sys.stdin = open('input.txt')
T = int(input())
print(T)
for tc in range(1, T+1):
    x = list(map(int, input().split()))
    sum_x = 0
    for i in range(len(x)):
        sum_x += x[i]
    b = sum_x/len(x)
    print('#{0} {1}'.format(tc, round(b)))