# 02. 도시 분할 계획 (p. 300)
# https://www.acmicpc.net/problem/1647
import sys

# Input
num_houses, num_paths = map(int, sys.stdin.readline().split())
paths = []
for _ in range(num_paths):
    data = list(map(int, sys.stdin.readline().split()))
    paths.append([data[2], data[0], data[1]])
paths.sort()


def find_parent(x):
    global parent
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    global parent
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 크루스칼 알고리즘
parent = [i for i in range(num_houses + 1)]
last_cost = 0
res = 0

for path in paths:
    cost, num1, num2 = path
    if find_parent(num1) != find_parent(num2):
        union(num1, num2)
        res += cost
        last_cost = cost

print(res - last_cost)