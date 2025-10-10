from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque(range(1, n+1))
count = 0

while len(dq) > 1:
    dq.popleft()
    dq.rotate(-1)
    count += 1

print(dq[0])