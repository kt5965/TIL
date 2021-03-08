T = int(input())

def solution(a):
    global d
    c = []
    for i in range(1, len(a)):
        visited = []
        if i not in visited:
            stack = []
            stack.append(a[i][0])
            while stack:
                b = stack.pop()
                if b not in visited:
                    visited.append(b)
                    stack.append(a[b][0])
            c.append(visited)

    for i in range(len(c)):
        if len(d) == 0:
            d.append(sorted(c[i]))
        c[i] = sorted(c[i])
        if c[i] not in d:
            d.append(c[i])
    return len(d)


for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    lis = list(range(1, len(N_list) + 1))
    a = [[] for _ in range(len(lis) + 1)]
    for i in range(1, len(lis)+1):
        a[i].append(N_list[i-1])
    d = []
    solution(a)
    print(len(d))



