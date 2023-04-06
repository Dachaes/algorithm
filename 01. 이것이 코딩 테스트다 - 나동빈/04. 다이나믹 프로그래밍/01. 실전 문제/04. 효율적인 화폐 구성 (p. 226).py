# 04. 효율적인 화폐 구성 (p. 226)

# Input
N = int(input())

cover = [-1, 1, 3]
for i in range(3, N + 1):
    cover.append(cover[i - 2] * 2 + cover[i - 1])

res = cover[N] % 796796
print(res)