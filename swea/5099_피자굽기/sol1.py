import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    oven, pizza = map(int, input().split())
    cheese = list(map(int, input().split()))
    number = [i+1 for i in range(pizza)]

    a = cheese[0:oven]
    b = number[0:oven]
    leftpizza = cheese[oven:]
    leftnumber = number[oven:]

    while len(a) !=1:
        a[0] //= 2
        if a[0]//2 == 0:
            a.pop(0)
            b.pop(0)
            if len(leftpizza)>0:
                a.append(leftpizza[0])
                leftpizza.pop(0)
                b.append(leftnumber[0])
                leftnumber.pop(0)
        else:
            a.append(a.pop(0))
            b.append(b.pop(0))

    print('#{} {}'.format(tc, b[0]))