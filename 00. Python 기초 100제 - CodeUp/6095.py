# 6095
n = int(input())
m = []
board = [[0 for j in range(19)] for i in range(19)]
for _ in range(n):
    m.append(list(map(int, input().split())))
for member in m:
    board[member[0] - 1][member[1] - 1] = 1

for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ')
    if i != 18:
        print("")
