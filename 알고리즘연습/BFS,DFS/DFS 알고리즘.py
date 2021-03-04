def dfs(graph, start):
    stack = []
    visited = [False for _ in range(100)]
    stack.append(start)
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = True
            stack += graph[now]

    if visited[now]:
        return 1
