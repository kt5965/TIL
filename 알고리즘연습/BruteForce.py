P = "is"
t = "This is a book!~"
M = len(P)
N = len(t)
i = 0
j = 0
while i < M and j < N:
    if P[i] != t[j]:
        j = j - i
        i = -1
    i += 1
    j += 1
if i == M:
    print('성공')
