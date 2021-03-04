N = 10

def solution(f, q, w, r, t, y):
    global ans, count
    for i in range(len(f)):
        for j in range(len(f)):
            if f[i][j] == 1:
                if i+4 < 10 and i+4 < 10 and y == [row[j:j+5] for row in f[i:i+5]] and count[4] != 0:
                    for k in range(5):
                        for l in range(5):
                            f[i+k][j+l] = 2
                    count[4] -= 1
                    ans += 1
    for i in range(len(f)):
        for j in range(len(f)):
            if f[i][j] == 1:
                if i+3 < 10 and i+3 < 10 and t == [row[j:j+4] for row in f[i:i+4]] and count[3] != 0:
                    for k in range(4):
                        for l in range(4):
                            f[i + k][j + l] = 2
                    count[3] -= 1
                    ans += 1
    for i in range(len(f)):
        for j in range(len(f)):
            if f[i][j] == 1:
                if i+2 < 10 and i+2 < 10 and r == [row[j:j+3] for row in f[i:i+3]] and count[2] != 0:
                    for k in range(3):
                        for l in range(3):
                            f[i + k][j + l] = 2
                    count[2] -= 1
                    ans += 1
    for i in range(len(f)):
        for j in range(len(f)):
            if f[i][j] == 1:
                if i+1 < 10 and i+1 < 10 and w == [row[j:j+2] for row in f[i:i+2]] and count[1] != 0:
                    for k in range(2):
                        for l in range(2):
                            f[i + k][j + l] = 2
                    count[1] -= 1
                    ans += 1
    for i in range(len(f)):
        for j in range(len(f)):
            if f[i][j] == 1:
                if q == [row[j:j+1] for row in f[i:i+1]] and count[0] != 0:
                    f[i][j] = 2

                    count[0] -= 1
                    ans += 1

    for i in range(len(f)):
        for j in range(len(f)):
            if f[i][j] == 1:
                ans = -1
    return ans


matrix = []
for i in range(10):
    matrix.append(list(map(int, input().split())))

a = [[1]]
b = [[1, 1], [1, 1]]
c = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
d = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
e = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
count = [5, 5, 5, 5, 5]
ans = 0
print(solution(matrix, a, b, c, d, e))