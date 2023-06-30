# 01. 팀 결성 (p. 298)
import sys

# Input
num_teams, num_operations = map(int, sys.stdin.readline().split())
operations = []
for _ in range(num_operations):
    operations.append(list(map(int, sys.stdin.readline().split())))

parent = [i for i in range(num_teams + 1)]


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


answer = []
for operation in operations:
    oper, num1, num2 = operation
    if oper == 0:
        union(num1, num2)
    elif oper == 1:
        if find_parent(num1) == find_parent(num2):
            answer.append("YES")
        else:
            answer.append("NO")

print(answer)

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
# res = [NO, NO, YES]