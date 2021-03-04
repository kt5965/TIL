def dfs(graph, start, visited):

    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited
