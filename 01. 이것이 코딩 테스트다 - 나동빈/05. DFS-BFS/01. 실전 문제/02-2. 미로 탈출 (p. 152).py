# 02. 미로 탈출 (p. 152)
from collections import deque

# Input
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

maze_deq = deque([(0, 0)])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while maze_deq:
    x, y = maze_deq[0][0], maze_deq[0][1]
    seq = maze[x][y]

    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if maze[next_x][next_y] == 1 and (next_x, next_y) != (0, 0):
                maze_deq.append((next_x, next_y))
                maze[next_x][next_y] = seq + 1
    maze_deq.popleft()

print(maze[n - 1][m - 1])

# for i in range(n):
#     print(maze[i])

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# res = 10

# 5 6
# 111111
# 111111
# 111111
# 111111
# 111111
# res = 10