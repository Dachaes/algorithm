# 01. 미래 도시 (p. 259)
import sys

# Input
num_company, num_path = map(int, sys.stdin.readline().split())
paths = []
for _ in range(num_path):
    paths.append(list(map(int, sys.stdin.readline().split())))
destination2, destination1 = map(int, sys.stdin.readline().split())


INF = int(1e9)
distance = [[INF] * (num_company + 1) for _ in range(num_company + 1)]

for k in range(1, num_company + 1):
    for i in range(1, num_company + 1):
        for j in range(1, num_company + 1):
            # 1. 입력 받은 path를 distance에 저장
            if k == i == j == 1:
                for path in paths:
                    distance[path[0]][path[1]] = 1
                    distance[path[1]][path[0]] = 1
            # 2. 같은 도시에서 같은 도시로 이동할 경우, distance에 0을 저장
            if i == j:
                distance[i][j] = 0
            # 3. 최소 거리를 계산한 후, distance에 저장
            else:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# 4. 결과값 계산
res = distance[1][destination1] + distance[destination1][destination2]
if res >= INF:
    print(-1)
else:
    print(res)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# res = 3

# 4 2
# 1 3
# 2 4
# 3 4
# res = -1