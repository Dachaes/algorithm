# 39. 화성 탐사 (p. 388)
import sys
import heapq
INF = int(1e9)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# Input
num_cases = int(sys.stdin.readline())
graphs = [[] for _ in range(num_cases)]
for i in range(num_cases):
    n = int(sys.stdin.readline())
    for j in range(n):
        graphs[i].append(list(map(int, sys.stdin.readline().split())))

answer = []
for graph in graphs:
    n = len(graph)
    distance = [[INF for _ in range(n)] for _ in range(n)]
    distance[0][0] = graph[0][0]
    q_dijkstra = []
    heapq.heappush(q_dijkstra, (distance[0][0], 0, 0))
    while q_dijkstra:
        dist, x, y = heapq.heappop(q_dijkstra)
        if dist > distance[x][y]:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q_dijkstra, (cost, nx, ny))
    answer.append(distance[n - 1][n - 1])

print(answer)

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# res = [20, 19, 36]