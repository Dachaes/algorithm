# 6064
x, y, z = map(int, input().split())
res = (x if (x < y) else y) if ((x if (x < y) else y) < z) else z
print(res)
