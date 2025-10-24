# BOJ 1753번 - 최단경로

## 문제 개요
- **문제 유형**: 최단경로 (다익스트라 알고리즘)
- **난이도**: Gold IV
- **핵심 개념**: 가중치가 있는 방향 그래프에서 한 정점에서 모든 정점까지의 최단거리

## 🔥 외워야 할 핵심 템플릿

### 1. 다익스트라 기본 구조
```python
import heapq
INF = float('inf')

def dijkstra(graph, start, V):
    distance = [INF] * (V + 1)
    distance[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, current_vertex = heapq.heappop(heap)
        
        if current_dist > distance[current_vertex]:
            continue
            
        for next_vertex, weight in graph[current_vertex]:
            new_dist = current_dist + weight
            if new_dist < distance[next_vertex]:
                distance[next_vertex] = new_dist
                heapq.heappush(heap, (new_dist, next_vertex))
    
    return distance
```

### 2. 입력 처리 (방향 그래프)
```python
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # 방향 그래프!
```

## ⚠️ 주의해야 할 점

### 1. **방향 그래프 vs 무방향 그래프**
```python
# 방향 그래프 (이 문제)
graph[u].append((v, w))

# 무방향 그래프라면
graph[u].append((v, w))
graph[v].append((u, w))  # 양방향 추가
```

### 2. **heapq 사용법**
```python
# 올바른 사용법
heap = [(거리, 정점)]
heapq.heappush(heap, (distance, vertex))
dist, vertex = heapq.heappop(heap)

# 잘못된 사용법 ❌
heap = [(정점, 거리)]  # 정점이 먼저 오면 안됨!
```

### 3. **이미 처리된 정점 확인**
```python
# 반드시 필요한 최적화!
if current_dist > distance[current_vertex]:
    continue  # 이미 더 짧은 경로로 처리됨
```

### 4. **INF 처리**
```python
# 출력 시 INF 확인
if distances[i] == INF:
    print("INF")
else:
    print(distances[i])
```

### 5. **배열 크기 주의**
```python
# 정점 번호가 1부터 시작
distance = [INF] * (V + 1)  # 0번 인덱스 포함
graph = [[] for _ in range(V + 1)]
```

## 🧠 암기해야 할 핵심 개념

### 1. **시간복잡도**
- **다익스트라**: O(E log V)
- **플로이드 워셜**: O(V³) - 모든 쌍 최단경로
- **벨만 포드**: O(VE) - 음수 가중치 허용

### 2. **다익스트라 vs 다른 알고리즘**
| 알고리즘 | 음수 가중치 | 시작점 | 시간복잡도 |
|---------|------------|--------|-----------|
| 다익스트라 | ❌ | 단일 | O(E log V) |
| 벨만 포드 | ✅ | 단일 | O(VE) |
| 플로이드 워셜 | ✅ | 모든 쌍 | O(V³) |

### 3. **우선순위 큐 원리**
- **최소 힙** 사용
- **가장 가까운 정점**부터 처리
- **그리디한 선택**이 최적해 보장

## 🎯 실수하기 쉬운 부분

### 1. **그래프 초기화 실수**
```python
# 잘못된 예
graph = [[] for _ in range(E + 1)]  # ❌ 간선 수로 초기화

# 올바른 예
graph = [[] for _ in range(V + 1)]  # ✅ 정점 수로 초기화
```

### 2. **가중치 순서 실수**
```python
# 입력: u v w
graph[u].append((v, w))  # ✅ (정점, 가중치)
graph[u].append((w, v))  # ❌ (가중치, 정점) - 잘못됨
```

### 3. **출력 범위 실수**
```python
# 1번부터 V번까지 출력
for i in range(1, V + 1):  # ✅
    print(distances[i])

for i in range(V):  # ❌ 0번부터 출력
    print(distances[i])
```

## 📝 문제 해결 단계

1. **입력 파싱**: V, E, K 받기
2. **그래프 구성**: 인접 리스트로 방향 그래프 생성
3. **다익스트라 실행**: 시작점 K에서 모든 정점까지 최단거리
4. **결과 출력**: 1번부터 V번까지 거리 (INF 처리)

## 🔗 관련 문제
- BOJ 1916: 최소비용 구하기
- BOJ 11779: 최소비용 구하기 2 (경로 복원)
- BOJ 1504: 특정한 최단 경로
