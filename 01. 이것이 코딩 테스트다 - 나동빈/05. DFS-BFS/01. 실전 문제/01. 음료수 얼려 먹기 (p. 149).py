# 01. 음료수 얼려 먹기 (p. 149)

# Input
n, m = map(int, input().split())
ice_mold = []
for i in range(n):
    ice_mold.append(list(map(int, input())))

def same_mold(row, col):
    if ice_mold[row][col] == 0:
        ice_mold[row][col] = 1
        if 0 <= row - 1:
            same_mold(row - 1, col)
        if row + 1 < n:
            same_mold(row + 1, col)
        if 0 <= col - 1:
            same_mold(row, col - 1)
        if col + 1 < m:
            same_mold(row, col + 1)

res = 0
for i in range(n):
    for j in range(m):
        if ice_mold[i][j] == 0:
            same_mold(i, j)
            res += 1

print(res)

# 4 5
# 00110
# 00011
# 11111
# 00000
# res = 3

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
# res = 8