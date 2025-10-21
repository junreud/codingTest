import sys
from collections import deque

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    # 큐에 (우선순위, 원래인덱스) 튜플로 저장
    
    # 방법 1: enumerate() 사용 (가독성 좋고 안전함) - 현재 사용
    queue = deque((priority, idx) for idx, priority in enumerate(priorities))
    
    # 방법 2: zip() 사용 (가장 빠름)
    # queue = deque(zip(priorities, range(N)))
    
    # 방법 3: 기존 for문 방식 (가장 직관적)
    # queue = deque()
    # for i in range(N):
    #     queue.append((priorities[i], i))
    
    count = 0  # 인쇄된 문서 수
    #(1,1) (2,2) (3,3) (4,4)
    while queue:
        current = queue.popleft()  # 현재 문서
        current_priority = current[0]
        current_index = current[1]
        
        # 현재 문서보다 중요도가 높은 문서가 있는지 확인
        
        # 방법 1: 기존 반복문 방식 (현재 사용) - 직관적이고 이해하기 쉬움
        has_higher_priority = False
        for doc in queue:
            if doc[0] > current_priority:
                has_higher_priority = True
                break
        
        # 방법 2: any() 함수 사용 (간결함)
        # has_higher_priority = any(doc[0] > current_priority for doc in queue)
        
        if has_higher_priority:
            # 더 중요한 문서가 있으면 맨 뒤로 보냄
            queue.append(current)
        else:
            # 가장 중요한 문서이므로 인쇄
            count += 1
            if current_index == M:
                # 우리가 찾는 문서라면 답 출력
                print(count)
                break
