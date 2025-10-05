import sys
input = sys.stdin.readline

n = int(input())
nums_list = []
for i in range(n):
    nums_list.append(int(input()))

nums_list.sort()

result = []

for i in range(n):
    result.append(nums_list[i] * (n - i))
print(max(result))