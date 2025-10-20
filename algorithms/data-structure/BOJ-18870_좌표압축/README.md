# BOJ 18870 - 좌표 압축

## 문제 개요
수직선 위의 N개 좌표를 좌표 압축하여, 각 좌표보다 작은 서로 다른 좌표의 개수로 변환하는 문제

## 핵심 포인트
1. **좌표 압축 개념**: 상대적 순서는 유지하면서 값의 범위를 줄이는 기법
2. **딕셔너리 매핑**: 원본 값과 압축된 값의 대응 관계
3. **정렬과 중복 제거**: `sorted(set())` 조합 활용

## 주요 학습 내용
- 좌표 압축 알고리즘의 이해
- Dictionary를 이용한 빠른 매핑
- enumerate() 함수 활용

## 해결 과정
1. 중복 제거 후 정렬: `sorted(set(coords))`
2. 딕셔너리 매핑: `{value: index for index, value in enumerate(unique_coords)}`
3. 원본 순서대로 변환: `[coord_map[coord] for coord in coords]`

## 시간복잡도
- 정렬: O(N log N)
- 매핑 생성: O(N)
- 결과 생성: O(N)
- 전체: O(N log N)

## 난이도
⭐⭐ (실버 2)