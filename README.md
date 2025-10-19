# 🚀 코딩테스트 문제 해결 모음집

백준 온라인 저지의 다양한 알고리즘 문제들을 해결한 코드와 설명을 모아놓은 저장소입니다.

## 📁 알고리즘별 폴더 구조

각 문제는 알고리즘 유형별로 분류되어 있으며, 다음과 같은 파일들을 포함합니다:
- `solution.py`: 문제 해결 코드
- `README.md`: 문제 설명, 핵심 포인트, 학습 내용

## 🔍 알고리즘 유형별 해결 문제들

### 📊 정렬 (Sorting) - `algorithms/sorting/`
- **[BOJ-2751 수정렬하기2](./algorithms/sorting/BOJ-2751_수정렬하기2)** - 실버5️⃣ 
  - 빠른 입출력과 O(N log N) 정렬
- **[BOJ-10814 나이순정렬](./algorithms/sorting/BOJ-10814_나이순정렬)** - 실버5️⃣
  - 안정 정렬(Stable Sort) 개념
- **[BOJ-10817 세수](./algorithms/sorting/BOJ-10817_세수)** - 브론즈3️⃣
  - 정렬을 이용한 중간값 찾기
- **[BOJ-2587 대표값2](./algorithms/sorting/BOJ-2587_대표값2)** - 브론즈2️⃣
  - 평균과 중앙값 계산
- **[BOJ-2752 세수정렬](./algorithms/sorting/BOJ-2752_세수정렬)** - 브론즈4️⃣
  - 기본 정렬과 출력 형식

### 🗂️ 자료구조 (Data Structure) - `algorithms/data-structure/`
- **[BOJ-1764 듣보잡](./algorithms/data-structure/BOJ-1764_듣보잡)** - 실버4️⃣
  - Set 교집합 연산
- **[BOJ-10815 숫자카드](./algorithms/data-structure/BOJ-10815_숫자카드)** - 실버5️⃣
  - Set을 이용한 빠른 검색
- **[BOJ-18870 좌표압축](./algorithms/data-structure/BOJ-18870_좌표압축)** - 실버2️⃣
  - 좌표 압축 기법
- **[BOJ-2164 카드2](./algorithms/data-structure/BOJ-2164_카드2)** - 실버4️⃣
  - 큐(Queue) 자료구조

### 🎯 그리디 알고리즘 (Greedy) - `algorithms/greedy/`
- **[BOJ-2217 로프](./algorithms/greedy/BOJ-2217_로프)** - 실버4️⃣
  - 그리디 알고리즘
- **[BOJ-1946 신입사원](./algorithms/greedy/BOJ-1946_신입사원)** - 실버1️⃣
  - 파레토 최적, 스카이라인 알고리즘

### 📚 스택 (Stack) - `algorithms/stack/`
- **[BOJ-9012 괄호](./algorithms/stack/BOJ-9012_괄호)** - 실버4️⃣
  - 스택을 이용한 괄호 검사
- **[BOJ-11703 제로](./algorithms/stack/BOJ-11703_제로)** - 실버4️⃣
  - 스택 기본 연산

### 🔍 탐색 (Search) - `algorithms/search/`
- **[BOJ-1920 수찾기](./algorithms/search/BOJ-1920_수찾기)** - 실버4️⃣
  - 이진 탐색 또는 해시 탐색

## 📚 주차별 정리

- **[1주차 정리](./주차별정리/1주차.ipynb)** - 1주차 학습 내용 정리

## 🎯 학습 목표

1. **기본기 다지기**: 정렬, 탐색 등 기본 알고리즘 마스터
2. **자료구조 활용**: Set, Dict 등을 이용한 효율적인 문제 해결
3. **시간복잡도 이해**: 효율적인 알고리즘 선택 능력 향상
4. **문제 해결 패턴**: 유형별 접근 방법 습득

## 💡 주요 학습 포인트

### 자주 사용하는 Python 패턴
```python
# 빠른 입출력
import sys
input = sys.stdin.readline

# Set을 이용한 빠른 검색
exists = num in number_set  # O(1)

# 정렬과 함께 사용하는 key 함수
sorted(items, key=lambda x: (x[0], x[1]))

# 좌표 압축
coord_map = {val: idx for idx, val in enumerate(sorted(set(coords)))}
```

### 시간복잡도 최적화
- 정렬: O(N log N)
- Set 검색: O(1)
- 그리디: O(N) 또는 O(N log N)

---

**💪 지속적인 학습과 성장을 위해 꾸준히 업데이트됩니다!**