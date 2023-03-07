# 6096
board = []
for _ in range(19):
    board.append(list(map(int, input().split())))
n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int, input().split())))
for member in m:
    for i in range(19):
        board[member[0] - 1][i] = (board[member[0] - 1][i]) ^ 1
        board[i][member[1] - 1] = (board[i][member[1] - 1]) ^ 1

for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ')
    if i != 18:
        print("")