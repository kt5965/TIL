import sys
sys.stdin = open('input.txt')
T = int(input())

# def solution(V, E, graph, S, G):
#     visited = [False for _ in range(V+1)]
#     to_visits = [S]
#
#     while to_visits:
#         current = to_visits.pop()
#         if not visited[current]:
#             visited[current] = True
#             to_visits += graph[current]
#     if visited[G] == True:
#         return 1
#     else:
#         return 0
def solution(V, graph, S, G):
    visited = [False for _ in range(V+1)]
    stack = [S]

    while stack:
        current = stack.pop()

        if visited[current] != True:
            visited[current] = True
            stack += graph[current]

    if visited[G] == True:
        return 1
    else:
        return 0




for tc in range(1, T+1):

    # Vertex, Edge의 갯수
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S,G = map(int, input().split())
    print(graph)
    print('#{} {}'.format(tc, solution(V, graph, S, G)))



