T = int(input())
count = 0
while True:
    if T % 5 == 0:
        count = count + T//5
        print(count)
        break
    T -= 3
    count += 1
    if T < 0:
        print('-1')
        break
