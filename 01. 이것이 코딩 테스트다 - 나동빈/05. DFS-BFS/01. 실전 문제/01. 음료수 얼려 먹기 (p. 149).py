# 01. 음료수 얼려 먹기 (p. 149)

# Input
n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input())))

def same_ice(row, col):
    if ice[row][col] == 0:
        ice[row][col] = 1
        if row + 1 < n:
            same_ice(row + 1, col)
        if col + 1 < m:
            same_ice(row, col + 1)

res = 0
for i in range(n):
    for j in range(m):
        if ice[i][j] == 0:
            ice[i][j] = 1
            res += 1
            if i + 1 < n:
                same_ice(i + 1, j)
            if j + 1 < m:
                same_ice(i, j + 1)


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