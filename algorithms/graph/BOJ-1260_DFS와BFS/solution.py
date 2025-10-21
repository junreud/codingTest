import sys
from collections import deque

input = sys.stdin.readline

def dfs(graph, v, visited, result):
    """DFS 재귀 구현"""
    visited[v] = True
    result.append(v)
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)

def bfs(graph, start):
    """BFS 큐 구현"""
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    result = []
    
    while queue:
        v = queue.popleft()
        result.append(v)
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

# 입력 처리
N, M, V = map(int, input().split())

# 그래프 초기화 (인덱스 1부터 사용)
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M): # graph = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]] 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프

# 작은 번호부터 방문하도록 정렬
for i in range(1, N + 1): 

    graph[i].sort()

# DFS 실행
visited_dfs = [False] * (N + 1)
dfs_result = []
dfs(graph, V, visited_dfs, dfs_result)

# BFS 실행
bfs_result = bfs(graph, V)

# 결과 출력
print(*dfs_result)
print(*bfs_result)
