def dfs(graph, V):
    stack = []
    stack.append(V)
    path = []
    while stack:
        a = stack.pop()
        if not visited[a]:
            visited[a] = True
            path.append(a)
            stack += sorted(graph[a])[::-1]
    return path




N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]
print(dfs(graph, V))