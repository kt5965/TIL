def bfs(graph, V):
    queue = []
    queue.append(V)
    visited = [False for _ in range(N + 1)]
    visited[V] = True
    print(V, end=' ')
    while queue:
        t = queue.pop(0)
        for i in graph[t]:
            if not visited[i]:
                queue.append(i)
                print(i, end=' ')
                visited[i] = True






N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)):
    graph[i] = sorted(graph[i])
bfs(graph, V)

