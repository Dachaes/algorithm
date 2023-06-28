import heapq
INF = int(1e9)
n = 3

distance = [[3 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        print(distance[i][j], end=' ')
    print('')
