# 6098
ant = [1, 1]
maze = []
for _ in range(10):
    maze.append(list(map(int, input().split())))

while True:
    # if ant eats food?
    if maze[ant[0]][ant[1]] == 2:
        maze[ant[0]][ant[1]] = 9
        break
    else:
        maze[ant[0]][ant[1]] = 9

    # ant is moving in maze
    if maze[ant[0]][ant[1] + 1] == 0 or maze[ant[0]][ant[1] + 1] == 2:
        ant[1] += 1
    elif maze[ant[0] + 1][ant[1]] == 0 or maze[ant[0] + 1][ant[1]] == 2:
        ant[0] += 1
    else:
        break

for i in range(10):
    for j in range(10):
        print(maze[i][j], end=' ')
    if i != 9:
        print("")