# 03. 커리큘럼 (p. 300)
# https://www.acmicpc.net/problem/1647
import sys
from collections import deque
# Input
num_lectures = int(sys.stdin.readline())
graph = []
for _ in range(num_lectures):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data[:-1])

print(graph)


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

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1