# BOJ-1012: 유기농 배추 🥬

## 📋 문제 정보
- **난이도**: Silver II
- **분류**: 그래프 이론, DFS, BFS, 연결 요소
- **알고리즘**: DFS(Depth-First Search) 또는 BFS(Breadth-First Search)
- **핵심 개념**: Connected Components (연결 요소) 찾기

## 🎯 문제 요약
배추밭에서 **인접한 배추들이 하나의 그룹**을 이룹니다. 각 그룹마다 배추흰지렁이 한 마리가 필요할 때, **총 몇 마리의 지렁이가 필요한지** 구하는 문제입니다.

### 입력 예시
```
2              # 테스트 케이스 수
10 8 17        # M(가로) N(세로) K(배추 개수)
0 0            # 배추 위치 (x, y)
1 0
1 1
...
```

### 출력 예시
```
5              # 첫 번째 테스트 케이스 답
1              # 두 번째 테스트 케이스 답
```

## 🔑 핵심 아이디어
1. **2D 그래프**에서 **연결된 요소의 개수** 구하기
2. 각 배추에서 DFS/BFS로 **연결된 모든 배추 방문**
3. 방문한 배추는 **0으로 마킹**하여 재방문 방지
4. DFS/BFS 실행 횟수 = **필요한 지렁이 수**

## 🚨 주의사항 및 함정

### 1. 좌표계 혼동 (가장 중요!)
```python
# ❌ 잘못된 이해
M, N, K = map(int, input().split())
field = [[0] * N for _ in range(M)]  # 틀림!

# ✅ 올바른 이해
M, N, K = map(int, input().split())  # M=가로(열), N=세로(행)
field = [[0] * M for _ in range(N)]  # N개 행, M개 열

# 입력 처리
x, y = map(int, input().split())
field[y][x] = 1  # field[행][열] = field[세로][가로]
```

**암기 포인트:**
- `M` = 가로 길이 = 열(column) 개수
- `N` = 세로 길이 = 행(row) 개수
- 입력 `(x, y)` → 배열 `[y][x]` (행열 순서 주의!)

### 2. RecursionError 해결
```python
import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 증가

# 또는 스택 기반 DFS 사용 (더 안전)
def dfs_iterative(field, start_x, start_y, M, N):
    stack = [(start_x, start_y)]
    # ... 구현
```

### 3. 범위 체크 순서
```python
# ✅ 올바른 순서
if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
    dfs(field, nx, ny, M, N)

# ❌ 잘못된 순서 (IndexError 발생 가능)
if field[nx][ny] == 1 and 0 <= nx < N and 0 <= ny < M:
```

## 💡 솔루션 비교

### Sol1: 기본 재귀 DFS
```python
def dfs(field, x, y, M, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    field[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
            dfs(field, nx, ny, M, N)
```

**장점:** 코드가 간단하고 직관적
**단점:** RecursionError 가능성

### Sol2: 스택 기반 DFS (권장)
```python
def dfs_iterative(field, start_x, start_y, M, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = [(start_x, start_y)]
    
    while stack:
        x, y = stack.pop()
        
        if x < 0 or x >= N or y < 0 or y >= M or field[x][y] == 0:
            continue
            
        field[x][y] = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
                stack.append((nx, ny))
```

**장점:** 재귀 에러 없음, 메모리 효율적
**단점:** 코드가 약간 복잡

## 🧠 외워야 할 패턴

### 1. DFS 기본 템플릿
```python
def dfs(graph, x, y):
    # 방문 처리
    graph[x][y] = 0
    
    # 4방향 탐색
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 조건:
            dfs(graph, nx, ny)
```

### 2. 연결 요소 카운팅 패턴
```python
result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:  # 미방문 노드 발견
            dfs(graph, i, j)   # 연결된 모든 노드 방문
            result += 1        # 요소 개수 증가
```

### 3. 2D 배열 초기화 패턴
```python
# M×N 2D 배열 (M=열, N=행)
field = [[0] * M for _ in range(N)]

# 또는 더 명확하게
field = [[0 for _ in range(M)] for _ in range(N)]
```

## ⚡ 시간복잡도 & 공간복잡도
- **시간복잡도**: O(M × N) - 모든 칸을 최대 1번씩 방문
- **공간복잡도**: O(M × N) - 2D 배열 + 스택 공간

## 🐛 디버깅 팁

### 1. 좌표 확인
```python
print(f"M={M}, N={N}")  # 가로, 세로 길이 확인
print(f"field 크기: {len(field)}×{len(field[0])}")  # 실제 배열 크기
```

### 2. 배추 위치 시각화
```python
for row in field:
    print(''.join(map(str, row)))
```

### 3. DFS 실행 추적
```python
def dfs(field, x, y, M, N):
    print(f"DFS 실행: ({x}, {y})")  # 디버깅 출력
    # ... 나머지 코드
```

## 🔄 비슷한 문제들
- **BOJ-2606**: 바이러스 (1차원 그래프)
- **BOJ-2667**: 단지번호붙이기 (2D 연결요소 + 크기)
- **BOJ-4963**: 섬의 개수 (8방향 탐색)
- **BOJ-1260**: DFS와 BFS (기본 그래프 탐색)

## 📚 학습 체크리스트
- [ ] 2D 좌표계 (x=열, y=행) 이해
- [ ] DFS 재귀 구현
- [ ] DFS 스택 구현
- [ ] RecursionError 해결법
- [ ] 연결 요소 카운팅 패턴
- [ ] 4방향 탐색 구현
- [ ] 방문 체크 및 백트래킹

## 🎯 핵심 암기사항
1. **좌표 변환**: 입력 `(x,y)` → 배열 `[y][x]`
2. **배열 크기**: `field = [[0] * M for _ in range(N)]`
3. **4방향**: `dx=[-1,1,0,0], dy=[0,0,-1,1]`
4. **재귀 제한**: `sys.setrecursionlimit(10000)`
5. **범위 체크**: 먼저 인덱스, 나중에 값 확인

---
*"2D 그래프 탐색의 정석을 마스터하자!" 🚀*
