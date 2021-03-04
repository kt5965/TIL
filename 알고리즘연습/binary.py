a = [0, 1, 7, 9, 15, 17, 19, 21, 25, 29, 36]
s = 0
e = len(a)-1
key = 29
while s <= e:
    mid = (s+e)//2
    if a[mid] == key:
        break
    elif a[mid] > key:
        e = mid
    else:
        s = mid
print(a[mid])