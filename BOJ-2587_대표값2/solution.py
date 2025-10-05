nums = [int(input()) for _ in range(5)]
print(sum(nums) // 5)  # 정수 나눗셈으로 소수점 제거
print(sorted(nums)[2])

# 연산자는 나눗셈 결과를 소수점 이하를 버리고 정수로 반환합니다.