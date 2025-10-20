import sys
input = sys.stdin.readline

nums_3 = list(map(int, input().split()))
print(' '.join(map(str, sorted(nums_3))))