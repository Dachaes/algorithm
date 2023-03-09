# 03. 1이 될 때까지 (p. 99)

# input
N, K = map(int, input().split())

res = 0
while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    res += 1

print(res)