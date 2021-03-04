import sys
sys.stdin = open('input.txt')
T = int(input())

def hanoi(T, a, b, c):
    if T == 1:
        print(a, b)
    else:
        hanoi(T - 1, a, c, b)
        print(a, b)
        hanoi(T - 1, c, b, a)
sum = 1
for i in range(T - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(T, 1, 3, 2)
