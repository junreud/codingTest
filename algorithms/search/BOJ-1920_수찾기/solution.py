import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_set = set(n_list)

m = int(input())
m_list = list(map(int, input().split()))

for num in m_list:
    if num in n_set:
        print(1)
    else:
        print(0)