n = int(input())
a = 2
while True:
    if n%a == 0:
        n = n/a
        print(a)
    else:
        a += 1
    if n == 1:
        break