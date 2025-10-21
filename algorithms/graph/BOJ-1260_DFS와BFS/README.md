# BOJ 1260 - DFS와 BFS

## 문제 개요
그래프를 DFS(깊이 우선 탐색)와 BFS(너비 우선 탐색)로 탐색하여 방문 순서를 출력하는 문제

## 🔥 핵심 요소들

### **1. 그래프 표현 방법**
- **인접 리스트 사용** (메모리 효율적)
- **양방향 그래프** 처리
- **정점 번호 1부터 시작** (인덱스 0은 사용하지 않음)

### **2. 중요한 조건**
> **"방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문"**

이 조건이 핵심! → **반드시 정렬 필요**

## 🎯 문제 해결 핵심 포인트

### **포인트 1: 그래프 구성**
```python
# 1. 인접 리스트 초기화 (N+1 크기)
graph = [[] for _ in range(N + 1)]

# 2. 양방향 간선 처리
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)  # a → b
    graph[b].append(a)  # b → a (양방향!)

# 3. 🔑 핵심! 반드시 정렬
for i in range(1, N + 1):
    graph[i].sort()  # 작은 번호부터 방문하도록
```

### **포인트 2: DFS 구현 (깊이 우선)**
```python
def dfs(graph, v, visited, result):
    visited[v] = True      # 방문 표시
    result.append(v)       # 결과에 추가
    
    # 인접 정점들을 작은 번호부터 방문
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)  # 재귀 호출
```

**DFS 특징:**
- **재귀 함수** 또는 **스택** 사용
- **깊이 우선**: 한 방향으로 끝까지 가본 후 되돌아옴
- **방문 즉시 표시**

### **포인트 3: BFS 구현 (너비 우선)**
```python
from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True  # 🔑 큐에 넣을 때 방문 표시!
    result = []
    
    while queue:
        v = queue.popleft()
        result.append(v)
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True  # 큐에 넣을 때 방문 표시
                queue.append(neighbor)
    
    return result
```

**BFS 특징:**
- **큐(deque)** 사용
- **너비 우선**: 같은 깊이 레벨을 모두 방문 후 다음 레벨
- **큐에 넣을 때 방문 표시** (중요!)

## ⚡ 자주하는 실수들

### **실수 1: 정렬하지 않기**
```python
# ❌ 정렬 안하면 결과가 다를 수 있음
graph[a].append(b)
graph[b].append(a)

# ✅ 반드시 정렬
for i in range(1, N + 1):
    graph[i].sort()
```

### **실수 2: BFS 방문 체크 시점**
```python
# ❌ 큐에서 뺄 때 방문 체크 (중복 가능)
v = queue.popleft()
if not visited[v]:
    visited[v] = True

# ✅ 큐에 넣을 때 방문 체크
if not visited[neighbor]:
    visited[neighbor] = True
    queue.append(neighbor)
```

### **실수 3: visited 배열 공유**
```python
# ❌ DFS와 BFS가 같은 visited 사용
visited = [False] * (N + 1)
dfs(graph, V, visited, dfs_result)
bfs(graph, V, visited)  # visited가 이미 True로 변경됨!

# ✅ 각각 별도의 visited 사용
visited_dfs = [False] * (N + 1)
dfs(graph, V, visited_dfs, dfs_result)
bfs_result = bfs(graph, V)  # bfs 함수 내부에서 새로운 visited 생성
```

## 🧠 알고리즘 동작 이해

### **예시: N=4, M=5, V=1**
```
간선: 1-2, 1-3, 1-4, 2-4, 3-4

그래프 구조:
    1
   /|\
  2 3 4
   \|/
    4
```

**인접 리스트:**
```python
graph[1] = [2, 3, 4]  # 정렬됨
graph[2] = [1, 4]
graph[3] = [1, 4]  
graph[4] = [1, 2, 3]
```

**DFS 과정 (시작: 1)**
```
1. 1 방문 → [2, 3, 4] 중 2 선택 (가장 작은 번호)
2. 2 방문 → [1, 4] 중 1은 이미 방문, 4 선택
3. 4 방문 → [1, 2, 3] 중 1,2는 방문됨, 3 선택
4. 3 방문 → 완료

결과: 1 2 4 3
```

**BFS 과정 (시작: 1)**
```
1. 큐: [1] → 1 방문, 인접 노드 [2, 3, 4] 큐에 추가
2. 큐: [2, 3, 4] → 2 방문, 4 추가하려 했지만 이미 큐에 있음
3. 큐: [3, 4] → 3 방문
4. 큐: [4] → 4 방문

결과: 1 2 3 4
```

## 🔍 DFS vs BFS 비교

| 구분 | DFS | BFS |
|------|-----|-----|
| **자료구조** | 스택 (재귀) | 큐 (deque) |
| **탐색 방식** | 깊이 우선 | 너비 우선 |
| **메모리** | 재귀 스택 | 큐 메모리 |
| **구현** | 재귀 함수 | 반복문 + 큐 |
| **용도** | 경로 탐색, 백트래킹 | 최단 거리, 레벨 순회 |

## 💻 완전한 구현 템플릿

```python
import sys
from collections import deque

input = sys.stdin.readline

def dfs(graph, v, visited, result):
    visited[v] = True
    result.append(v)
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)

def bfs(graph, start):
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

# 그래프 구성
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 🔑 핵심: 정렬
for i in range(1, N + 1):
    graph[i].sort()

# 실행
visited_dfs = [False] * (N + 1)
dfs_result = []
dfs(graph, V, visited_dfs, dfs_result)

bfs_result = bfs(graph, V)

# 출력
print(*dfs_result)
print(*bfs_result)
```

## 🎲 체크리스트

### **구현 전 확인사항:**
- [ ] 인접 리스트로 그래프 표현
- [ ] 양방향 간선 처리
- [ ] **정렬 반드시 포함**
- [ ] DFS는 재귀로, BFS는 큐로
- [ ] 각각 별도의 visited 배열 사용
- [ ] BFS에서 큐에 넣을 때 방문 표시

## 시간복잡도
- **DFS**: O(V + E) - 모든 정점과 간선을 한 번씩 방문
- **BFS**: O(V + E) - 모든 정점과 간선을 한 번씩 방문
- **정렬**: O(V × E log E) - 각 정점의 인접 리스트 정렬

## 난이도
⭐⭐ (실버 2)

---
**💡 핵심**: 그래프 기본 탐색 문제. **정렬**이 가장 중요한 포인트!
