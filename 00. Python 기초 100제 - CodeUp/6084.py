# 6084
h, n, c, s = map(int, input().split())
res = h * n * c * s / 8 / 1024 / 1024
print(f"{res:.1f} MB")
