# 02. 미로 탈출 (p. 152)

# Input
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

def is_monster(row, col, seq):
    if maze[row][col] == 1:
        maze[row][col] = seq
        if 0 <= row - 1 and (row - 1, col) != (0, 0):
            is_monster(row - 1, col, seq + 1)
        if row + 1 < n and (row + 1, col) != (0, 0):
            is_monster(row + 1, col, seq + 1)
        if 0 <= col - 1 and (row, col - 1) != (0, 0):
            is_monster(row, col - 1, seq + 1)
        if col + 1 < m and (row, col + 1) != (0, 0):
            is_monster(row, col + 1, seq + 1)

is_monster(0, 0, 1)
print(maze[n - 1][m - 1])

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# res = 10