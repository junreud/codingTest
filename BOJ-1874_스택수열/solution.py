n = int(input())

num_list = [int(input()) for _ in range(n)] # [1, 2, 5, 3, 4]
current = 1 # 6
stack = [] # 3, 4
result = [] # +, -, +, -, +, +, +, -

for num in num_list: # 3
    while num >= current:
        stack.append(current)
        result.append("+")
        current += 1
    if stack[-1] == num:
        result.append("-")
        stack.pop()
    else:
        print("NO")


for m in result:
    print(m)