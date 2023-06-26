# 02. 전보 (p. 262)
import sys, heapq

# Input
num_company, num_path, start = map(int, sys.stdin.readline().split())
paths = [[] for _ in range(num_company + 1)]
for _ in range(num_path):
    data = list(map(int, sys.stdin.readline().split()))
    paths[data[0]].append([data[1], data[2]])


INF = int(1e9)
distance = [INF] * (num_company + 1)

# 1. 다익스트라 알고리즘
q_dijkstra = []
heapq.heappush(q_dijkstra, (0, start))
distance[start] = 0
while q_dijkstra:
    dist, pos = heapq.heappop(q_dijkstra)
    if distance[pos] < dist:
        continue
    for path in paths[pos]:
        next_pos, next_dist = path[0], dist + path[1]
        if next_dist < distance[next_pos]:
            distance[next_pos] = next_dist
            heapq.heappush(q_dijkstra, (dist, next_pos))
            
# 2. 결과 도출        
count = 0
max_dist = 0
for i in range(num_company + 1):
    if distance[i] != 0 and distance[i] != INF:
        count += 1
    if distance[i] != INF and max_dist < distance[i]:
        max_dist = distance[i]
        
print(count, max_dist)