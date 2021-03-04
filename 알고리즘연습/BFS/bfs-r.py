def dfs(graph, V):
    stack = []
    stack.append(V)
    path = []
    while stack:
        a = stack.pop(0)
        if not visited[a]:
            visited[a] = True
            path.append(a)
            stack += graph[a]
    return path




N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)):
    graph[i] = sorted(graph[i])
visited = [False for _ in range(N+1)]
print(dfs(graph, V))