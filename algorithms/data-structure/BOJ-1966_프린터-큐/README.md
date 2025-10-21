# BOJ 1966 - 프린터 큐

## 문제 개요
여러 문서가 프린터 큐에 있을 때, 중요도에 따라 우선순위를 정해서 인쇄하는 문제. 특정 문서가 몇 번째로 인쇄되는지 찾기

## 🔥 핵심 아이디어

### **프린터 동작 원리**
1. 큐에서 문서를 하나씩 꺼냄
2. **현재 문서보다 중요도가 높은 문서가 뒤에 있으면** → 맨 뒤로 보냄
3. **현재 문서가 가장 중요하면** → 인쇄!
4. 우리가 찾는 문서가 몇 번째로 인쇄되는지 확인

## 🧠 알고리즘 이해

### **예시: 문서 4개, 찾는 문서는 2번째**
```
입력: N=4, M=2
중요도: [2, 1, 4, 3]
목표: 인덱스 2인 문서(중요도 4)가 몇 번째로 인쇄되는가?

큐 초기화: [(2,0), (1,1), (4,2), (3,3)]

1단계: (2,0) 꺼냄 → (4,2), (3,3)이 더 중요 → 뒤로 보냄
큐: [(1,1), (4,2), (3,3), (2,0)]

2단계: (1,1) 꺼냄 → (4,2), (3,3), (2,0) 모두 더 중요 → 뒤로 보냄
큐: [(4,2), (3,3), (2,0), (1,1)]

3단계: (4,2) 꺼냄 → 가장 중요함 → 인쇄! (1번째)
목표 문서 발견! 답: 1
```

## 💻 핵심 구현 코드

### **자료구조 설계**
```python
from collections import deque

# (중요도, 원래인덱스) 튜플로 저장하여 어떤 문서인지 추적
queue = deque((priority, idx) for idx, priority in enumerate(priorities))
```

### **핵심 로직**
```python
while queue:
    current = queue.popleft()
    current_priority = current[0]
    current_index = current[1]
    
    # 더 중요한 문서가 있는지 확인
    has_higher_priority = False
    for doc in queue:
        if doc[0] > current_priority:
            has_higher_priority = True
            break
    
    if has_higher_priority:
        queue.append(current)  # 뒤로 보냄
    else:
        count += 1  # 인쇄!
        if current_index == M:  # 찾는 문서인지 확인
            print(count)
            break
```

## 🎯 여러 구현 방법 비교

### **1. 큐 생성 방법들**
```python
# 방법 1: enumerate() - 가독성 좋고 안전함 ⭐
queue = deque((priority, idx) for idx, priority in enumerate(priorities))

# 방법 2: zip() - 가장 빠름
queue = deque(zip(priorities, range(N)))

# 방법 3: 기존 for문 - 가장 직관적
queue = deque()
for i in range(N):
    queue.append((priorities[i], i))
```

### **2. 중요도 비교 방법들**
```python
# 방법 1: 기존 반복문 - 직관적이고 디버깅 용이 ⭐
has_higher_priority = False
for doc in queue:
    if doc[0] > current_priority:
        has_higher_priority = True
        break

# 방법 2: any() 함수 - 간결함
has_higher_priority = any(doc[0] > current_priority for doc in queue)
```

## 🔍 상세 분석

### **시뮬레이션 과정**
1. **튜플 활용**: `(중요도, 인덱스)`로 원래 위치 추적
2. **우선순위 비교**: 현재 문서와 큐의 모든 문서 비교
3. **조건부 처리**: 
   - 더 중요한 문서 있음 → 현재 문서를 맨 뒤로
   - 가장 중요함 → 인쇄 후 카운트 증가
4. **목표 달성**: 찾는 문서가 인쇄되면 순서 출력

### **핵심 변수들**
- `queue`: 문서들을 저장하는 deque
- `current`: 현재 처리 중인 문서 `(중요도, 인덱스)`
- `count`: 지금까지 인쇄된 문서 수
- `M`: 우리가 찾는 문서의 원래 인덱스

## 🚀 최적화 포인트

### **1. 조기 종료 (Early Exit)**
```python
# 더 중요한 문서를 찾으면 즉시 중단
for doc in queue:
    if doc[0] > current_priority:
        has_higher_priority = True
        break  # 즉시 종료로 성능 향상
```

### **2. 효율적인 자료구조**
- **deque 사용**: `popleft()`, `append()` 모두 O(1)
- **튜플 저장**: 메모리 효율적이고 불변성 보장

## 💡 주의사항

### **1. 인덱스 추적**
```python
# ❌ 중요도만 저장하면 어떤 문서인지 구분 불가
queue = deque(priorities)

# ✅ (중요도, 인덱스) 튜플로 저장
queue = deque((priority, idx) for idx, priority in enumerate(priorities))
```

### **2. 무한 루프 방지**
```python
# 반드시 찾는 문서가 인쇄될 때 break
if current_index == M:
    print(count)
    break  # 중요!
```

## 🔗 관련 개념

### **큐 시뮬레이션 패턴**
- **BFS**: 너비 우선 탐색
- **작업 스케줄링**: 우선순위 기반 처리
- **버퍼링**: 데이터 임시 저장 후 순차 처리

### **우선순위 큐와의 차이**
- **우선순위 큐**: 자동으로 정렬됨 (heapq)
- **이 문제**: 수동으로 비교하며 시뮬레이션

## 🎲 테스트 케이스

### **예시 1**
```
입력:
1
4 2
1 2 3 4

출력: 2
```

### **예시 2**
```
입력:
1
6 0
1 1 9 1 1 1

출력: 5
```

## 시간복잡도
- **시간복잡도**: O(N²) - 최악의 경우 각 문서마다 모든 문서 비교
- **공간복잡도**: O(N) - 큐에 N개 문서 저장

## 난이도
⭐⭐ (실버 3)

---
**💡 핵심**: 큐의 FIFO 특성을 이용하되, 우선순위에 따라 조건부로 뒤로 보내는 시뮬레이션 문제!
    