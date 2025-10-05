import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 두 집합을 만들어서 교집합 구하기
no_heard = set()
for _ in range(n):
    no_heard.add(input().strip())

no_see = set()
for _ in range(m):
    no_see.add(input().strip())

# 교집합 구하기 - O(min(n, m))
results = sorted(no_heard & no_see)

print(len(results))
print('\n'.join(results))

"""
=== set() 자료구조 완전 분석 ===

1. 🎯 set의 정의
   - 중복을 허용하지 않는 자료구조 (수학의 집합과 동일)
   - 해시테이블(Hash Table) 기반으로 구현
   - 순서가 없음 (unordered)

2. ⚡ 성능 특징
   - 검색(in): O(1) - 평균 시간복잡도 (해시 직접 접근)
   - 추가(add): O(1) - 평균 시간복잡도
   - 삭제(remove): O(1) - 평균 시간복잡도
   - 리스트 검색: O(n) vs set 검색: O(1) → 엄청난 성능 차이!

3. 🔧 주요 메서드와 연산
   기본 메서드:
   - set.add(item): 원소 추가
   - set.remove(item): 원소 제거 (없으면 KeyError)
   - set.discard(item): 원소 제거 (없어도 에러 없음)
   - item in set: 원소 존재 확인 O(1)
   - len(set): 집합 크기
   
   집합 연산:
   - A & B (교집합): A와 B 모두에 있는 원소
   - A | B (합집합): A 또는 B에 있는 원소
   - A - B (차집합): A에는 있지만 B에는 없는 원소
   - A ^ B (대칭차집합): A와 B 중 하나에만 있는 원소

4. 💡 언제 사용하면 좋을까?
   ✅ 중복 제거가 필요할 때
   ✅ 빠른 검색이 필요할 때 (in 연산)
   ✅ 교집합, 합집합 등 집합 연산이 필요할 때
   ✅ 대용량 데이터에서 존재성 확인이 필요할 때
   
   ❌ 순서가 중요할 때 (순서 없음)
   ❌ 중복 값을 보관해야 할 때
   ❌ 인덱싱이 필요할 때 (set[0] 불가능)

5. 🔍 실제 예시
   # 기본 사용법
   fruits = {"apple", "banana", "cherry"}
   fruits.add("orange")
   print("apple" in fruits)  # True, O(1)
   
   # 리스트 vs set 성능 비교
   big_list = list(range(1000000))
   big_set = set(range(1000000))
   
   # 리스트에서 검색: 최악 O(n) = 100만번 비교
   if 999999 in big_list:  # 느림
       pass
   
   # set에서 검색: O(1) = 1번 해시 계산
   if 999999 in big_set:   # 빠름
       pass

6. 🚀 이 문제에서 set을 사용한 이유
   - 듣도 못한 사람 목록: no_heard (set)
   - 보도 못한 사람 목록: no_see (set)
   - 교집합 연산: no_heard & no_see
   
   성능 개선:
   - 리스트 방식: O(n × m) = 500,000 × 500,000 = 시간초과
   - set 방식: O(n + m) = 500,000 + 500,000 = 빠름!

7. ⚠️ 주의사항
   - set에는 해시 가능한(hashable) 객체만 저장 가능
   - 리스트, 딕셔너리는 set에 넣을 수 없음
   - 문자열, 숫자, 튜플은 가능
   
   # 가능
   valid_set = {1, "hello", (1, 2)}
   
   # 불가능 (TypeError 발생)
   # invalid_set = {[1, 2], {"key": "value"}}

8. 🎯 코딩테스트 활용 팁
   - 중복 제거: list(set(data))
   - 빠른 존재성 확인: item in my_set
   - 교집합 찾기: set1 & set2
   - 합집합: set1 | set2
   - 차집합: set1 - set2
   
   특히 "두 그룹에서 공통 원소 찾기" 문제에서 매우 유용!
"""