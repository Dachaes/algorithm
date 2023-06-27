# 37. 플로이드 (p. 385)
# https://www.acmicpc.net/problem/11404
import sys

# Input
num_city = int(sys.stdin.readline())
num_bus = int(sys.stdin.readline())
graph = []
for _ in range(num_bus):
    graph.append(list(map(int, sys.stdin.readline().split())))


INF = int(1e9)
cost = [([INF] * (num_city + 1)) for _ in range(num_city + 1)]

for k in range(1, num_city + 1):
    for i in range(1, num_city + 1):
        for j in range(1, num_city + 1):
            if k == i == j == 1:
                for g in graph:
                    cost[g[0]][g[1]] = min(cost[g[0]][g[1]], g[2])
            if k == 1 and i == j:
                cost[i][j] = 0
            elif i != j:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(1, num_city + 1):
    for j in range(1, num_city + 1):
        if cost[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print('')