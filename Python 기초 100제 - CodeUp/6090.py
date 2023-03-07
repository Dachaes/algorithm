# 6090
a, m, d, n = map(int, input().split())
res = a
for i in range(1, n):
    res = res * m + d
print(res)
