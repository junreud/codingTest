# BOJ 1874 - 스택 수열

## 문제 개요
1부터 n까지의 수를 스택에 push/pop 연산을 통해 주어진 수열을 만들 수 있는지 확인하고, 가능하다면 연산 과정을 출력하는 문제

## 🔥 핵심 아이디어

### **스택의 LIFO 특성 이용**
- 1부터 n까지 **순서대로만** push 가능
- 스택에서는 **맨 위 원소만** pop 가능
- push 연산: `+`, pop 연산: `-`로 표현

## 🧠 알고리즘 이해하기

### **예시: 목표 수열 [4, 3, 6, 8, 7, 5, 2, 1]**

```
=== 4를 만들기 ===
1 push → stack: [1], 연산: +
2 push → stack: [1,2], 연산: + +  
3 push → stack: [1,2,3], 연산: + + +
4 push → stack: [1,2,3,4], 연산: + + + +
4 pop  → stack: [1,2,3], 연산: + + + + -, 출력: 4

=== 3을 만들기 ===
스택 맨 위가 3 → 3 pop
stack: [1,2], 연산: + + + + - -, 출력: 4, 3

=== 6을 만들기 ===  
5 push → stack: [1,2,5], 연산: + + + + - - +
6 push → stack: [1,2,5,6], 연산: + + + + - - + +
6 pop  → stack: [1,2,5], 연산: + + + + - - + + -, 출력: 4,3,6
```

### **불가능한 경우**
```
목표: [3, 1]

3을 만들기: 1,2,3 push → 3 pop
stack: [1,2], 출력: 3

1을 만들기: 스택 맨 위가 2인데 1을 원함
→ 2를 먼저 빼야 1에 접근 가능하지만 목표는 1
→ 불가능! "NO" 출력
```

## 💻 구현 코드

### **핵심 로직**
```python
stack = []
result = []
current = 1  # 다음에 push할 숫자

for target in num_list:
    # 1. target까지 순서대로 push
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1
    
    # 2. 스택 맨 위가 target이면 pop
    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        # 3. 불가능한 경우
        print("NO")
        break
```

### **전체 구현**
```python
import sys
input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1
possible = True

for target in num_list:
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1
    
    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    for op in result:
        print(op)
else:
    print("NO")
```

## 🎯 핵심 포인트 (외워야 할 것)

### 1. **변수 역할**
- `current`: 1부터 n까지 순서대로 push할 숫자 추적
- `stack`: 실제 스택 구조
- `result`: +/- 연산 기록

### 2. **핵심 조건**
```python
# target까지 push (순서대로)
while current <= target:
    stack.append(current)
    result.append('+')
    current += 1

# 스택 맨 위 확인 후 pop
if stack and stack[-1] == target:
    stack.pop()
    result.append('-')
```

### 3. **불가능 판단**
- 스택 맨 위가 target과 다르면 불가능
- target보다 큰 수가 스택 맨 위에 있으면 target에 접근 불가

## 🔍 디버깅 팁

### **시뮬레이션으로 확인**
```python
# 각 단계별 상태 출력
print(f"target: {target}")
print(f"current: {current}")  
print(f"stack: {stack}")
print(f"result: {result}")
print("---")
```

### **자주 하는 실수**
1. `current` 변수를 매번 1로 초기화
2. 스택이 비어있을 때 `stack[-1]` 접근
3. push/pop 순서 헷갈리기

## 관련 문제 패턴
- **괄호 문제**: 짝 맞추기
- **히스토그램**: 스택으로 최적화
- **NGE**: Next Greater Element

## 시간복잡도
- **시간복잡도**: O(N) - 각 숫자를 한 번씩만 push/pop
- **공간복잡도**: O(N) - 스택과 결과 배열

## 난이도
⭐⭐⭐ (실버 2)

---
**💡 핵심**: 스택의 LIFO 특성을 이해하고, 순서대로 push하면서 목표 수열을 만들 수 있는지 시뮬레이션하는 문제!
