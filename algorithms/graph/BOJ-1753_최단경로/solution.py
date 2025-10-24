import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(graph, start, V):
    """다익스트라 알고리즘으로 최단경로 구하기"""
    # 거리 배열 초기화
    distance = [INF] * (V + 1)
    distance[start] = 0
    
    # 우선순위 큐 (거리, 정점)
    heap = [(0, start)]
    
    while heap:
        # 현재 최단거리가 가장 짧은 정점 선택
        current_dist, current_vertex = heapq.heappop(heap)
        
        # 이미 처리된 정점이면 무시
        if current_dist > distance[current_vertex]:
            continue
            
        # 인접한 정점들 확인
        for next_vertex, weight in graph[current_vertex]:
            new_dist = current_dist + weight
            
            # 더 짧은 경로를 발견한 경우
            if new_dist < distance[next_vertex]:
                distance[next_vertex] = new_dist
                heapq.heappush(heap, (new_dist, next_vertex))
    
    return distance

def solve():
    # 입력
    V, E = map(int, input().split())  # 정점 수, 간선 수
    K = int(input())  # 시작 정점
    
    # 그래프 초기화 (인접 리스트)
    graph = [[] for _ in range(V + 1)]
    
    # 간선 정보 입력
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))  # u에서 v로 가는 가중치 w
    
    # 다익스트라 실행
    distances = dijkstra(graph, K, V)
    
    # 결과 출력
    for i in range(1, V + 1):
        if distances[i] == INF:
            print("INF")
        else:
            print(distances[i])

solve()