# 40. 숨바꼭질 (p. 390)
import sys
import heapq
INF = int(1e9)

# Input
start = 1
num_rooms, num_paths = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(num_rooms + 1)]
for i in range(num_paths):
    data1, data2 = map(int, sys.stdin.readline().split())
    if data2 not in graph[data1]:
        graph[data1].append(data2)
    if data1 not in graph[data2]:
        graph[data2].append(data1)

distance = [INF for _ in range(num_rooms + 1)]
distance[1] = 0

# 다익스트라 알고리즘
q_dijkstra = []
heapq.heappush(q_dijkstra, (0, start))
while q_dijkstra:
    dist, pos = heapq.heappop(q_dijkstra)
    if dist > distance[pos]:
        continue
    for next_pos in graph[pos]:
        cost = dist + 1
        if cost < distance[next_pos]:
            distance[next_pos] = cost
            heapq.heappush(q_dijkstra, (cost, next_pos))

distance.pop(0)
max_value = max(distance)
max_index = distance.index(max_value) + 1
count_max = distance.count(max_value)
answer = [max_index, max_value, count_max]

print(answer)

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
# res = 4 2 3