import sys
sys.stdin = open('input.txt')

def dfs(graph, start, visited):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    if 99 in visited:
        return 1
    else:
        return 0







for tc in range(1, 11):
    A, B = map(int, input().split())
    graph = [[] for _ in range(100)]
    C = list(map(int,input().split()))
    for i in range(0, len(C), 2):
        graph[C[i]].append(C[i+1])
    visited = []
    print(graph)
    print('#{} {}'.format(tc, dfs(graph, 0, visited)))
