import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    applicants = []
    for _ in range(n):
        a, b = map(int, input().split())
        applicants.append((a, b))  # (첫번째 숫자, 두번째 숫자)
    
    # 첫번째 숫자 기준으로 정렬
    applicants = sorted(applicants, key=lambda x: x[0])
    count = set()
    for j in range(n):
        for k in range(j + 1, n):
            if applicants[j][1] > applicants[k][1]:
                count.add(applicants[k])
                break
    print(len(count)+1)