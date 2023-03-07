# 6094
n = int(input())
m = list(map(int, input().split()))
MIN = m[0]
for member in m:
    if member < MIN:
        MIN = member
print(MIN)
