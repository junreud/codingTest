import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    m = int(input())
    if m == 0:
        nums.pop()
    else:
        nums.append(m)

print(sum(nums))