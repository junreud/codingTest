# 🚀 코딩테스트 문제 해결 모음집

백준 온라인 저지의 다양한 알고리즘 문제들을 해결한 코드와 설명을 모아놓은 저장소입니다.

## 📁 문제별 폴더 구조

각 문제는 독립적인 폴더로 구성되어 있으며, 다음과 같은 파일들을 포함합니다:
- `solution.py`: 문제 해결 코드
- `README.md`: 문제 설명, 핵심 포인트, 학습 내용

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