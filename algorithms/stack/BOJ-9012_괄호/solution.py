import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    ps = input().rstrip()
    stack = []
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(p)
                break
    if stack:
        print("NO")
    else:
        print("YES")