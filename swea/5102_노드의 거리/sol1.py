import sys
sys.stdin = open('input.txt')

def bfs(graph, S, G, visited, leng):
    queue = []
    queue.append(S)
    visited[S] = True
    while queue:
        a = queue.pop(0)
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                leng[i] = leng[a] + 1
    return leng



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    leng = [0] * (V+1)
    for i in range(E):
        b, c = map(int, input().split())
        graph[b].append(c)
        graph[c].append(b)
    S, G = map(int, input().split())
    visited = [False] * (V + 1)
    bfs(graph, S, G, visited, leng)
    print('#{} {}'.format(tc, leng[G]))
