# BOJ 10845 - 큐

## 문제 개요
큐 자료구조의 기본 연산들을 구현하는 문제

## 🔥 외워야 할 핵심 사항들

### 1. **큐 import와 생성 (필수 암기)**
```python
from collections import deque  # 반드시 외우기!
queue = deque()                # 큐 생성
```

### 2. **큐 기본 연산 (반드시 외워야 함)**
```python
# enqueue (뒤에 추가)
queue.append(x)

# dequeue (앞에서 제거)
front = queue.popleft()  # ⚠️ popleft() 주의!

# 크기 확인
len(queue)

# 비어있는지 확인
if queue:         # 큐에 데이터 있음
if not queue:     # 큐가 비어있음

# 맨 앞 요소 확인 (제거 안함)
queue[0]

# 맨 뒤 요소 확인 (제거 안함)
queue[-1]
```

### 3. **BOJ-10845 구현 템플릿 (통째로 외우기)**
```python
import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
n = int(input())

for _ in range(n):
    command = input().split()
    
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        print(queue.popleft() if queue else -1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if not queue else 0)
    elif command[0] == "front":
        print(queue[0] if queue else -1)
    elif command[0] == "back":
        print(queue[-1] if queue else -1)
```

## 💡 실수하기 쉬운 포인트 (암기 필수)

### 1. **pop vs popleft**
```python
# ❌ 틀린 방법
queue.pop()      # 뒤에서 제거 (스택)

# ✅ 올바른 방법  
queue.popleft()  # 앞에서 제거 (큐)
```

### 2. **빈 큐 처리**
```python
# ❌ 에러 발생
if len(queue) == 0:
    return -1
else:
    return queue.popleft()

# ✅ 간단한 방법
return queue.popleft() if queue else -1
```

### 3. **empty 명령어**
```python
# ❌ 헷갈리기 쉬운 방법
if len(queue) == 0:
    print(1)
else:
    print(0)

# ✅ 외워둘 패턴
print(1 if not queue else 0)
```

## 🚀 다른 문제에서도 쓰는 큐 패턴들

### 1. **BFS 탐색**
```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()  # 큐에서 꺼내기
        
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)  # 큐에 추가
```

### 2. **레벨별 처리**
```python
from collections import deque

queue = deque([start])
level = 0

while queue:
    size = len(queue)  # 현재 레벨 크기
    
    for _ in range(size):  # 현재 레벨만 처리
        node = queue.popleft()
        # 처리...
        
        # 다음 레벨 추가
        queue.append(next_node)
    
    level += 1
```

## ⚡ 시간복잡도 (외워두기)

| 연산 | deque | list |
|------|-------|------|
| **append()** | O(1) | O(1) |
| **popleft()** | **O(1)** | O(n) ❌ |
| **pop()** | O(1) | O(1) |
| **len()** | O(1) | O(1) |

## 🎯 핵심 암기 사항

1. **`from collections import deque`** - 반드시 외우기
2. **`queue.popleft()`** - pop()이 아니라 popleft()!
3. **`if queue:`** - 빈 큐 체크하는 가장 간단한 방법
4. **BFS는 큐, DFS는 스택** - 탐색 알고리즘 선택

## 난이도
⭐⭐ (실버 4)

---
**💡 Tip**: 이 템플릿을 통째로 외워두면 큐 관련 모든 문제에서 활용 가능!
