# 6097
h, w = map(int, input().split())
n = int(input())
stick = []
board = [[0 for j in range(w)] for i in range(h)]
for _ in range(n):
    stick.append(list(map(int, input().split())))

for mem in stick:
    for i in range(mem[0]):
        try:
            if mem[1] == 1:
                board[mem[2] - 1 + i][mem[3] - 1] = 1
            else:
                board[mem[2] - 1][mem[3] - 1 + i] = 1
        except IndexError:
            pass

for i in range(h):
    for j in range(w):
        print(board[i][j], end=' ')
    if i != (h - 1):
        print("")
