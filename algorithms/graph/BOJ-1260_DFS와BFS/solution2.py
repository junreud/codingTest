import sys
from collections import deque
input = sys.stdin.readline
#               3
def bfs(graph, start): # [] [2, 3] [1, 5] [1, 4] [3, 5] [2, 4]
    queue = deque([start])
    bfs_list = [False] * (N + 1) # [False], [True], [False], [True], [True], [False]
    bfs_list[start] = True
    result = [] #[3, 1, 4]

    while queue:
        v = queue.popleft()
        result.append(v)
        for i in graph[v]: # 2, 3, 4
            if not bfs_list[i]:
                bfs_list[i] = True
                queue.append(i)
    return result

def dfs(graph, start, visited, result):
    visited[start] = True
    result.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited, result)
    return result

N, M, V = map(int, input().split())


graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

# DFS 실행
visited = [False] * (N + 1)
result = []
dfs_result = dfs(graph, V, visited, result)
print(' '.join(map(str, dfs_result)))

# BFS 실행
bfs_result = bfs(graph, V)
print(' '.join(map(str, bfs_result)))