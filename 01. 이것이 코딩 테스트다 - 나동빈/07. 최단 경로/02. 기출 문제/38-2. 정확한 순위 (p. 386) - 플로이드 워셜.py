# 38. 정확한 순위 (p. 386)
import sys
INF = int(1e9)

# Input
num_students, num_comparisons = map(int, sys.stdin.readline().split())
graph = []
for _ in range(num_comparisons):
    graph.append(list(map(int, sys.stdin.readline().split())))

rank = [[INF] * (num_students + 1) for _ in range(num_students + 1)]
for k in range(1, num_students + 1):
    for i in range(1, num_students + 1):
        for j in range(1, num_students + 1):
            # 플로이드 워셜 알고리즘
            if k == i == j == 1:
                for g in graph:
                    rank[g[0]][g[1]] = 1
            if k == 1 and i == j:
                rank[i][j] = 0
            elif i != j:
                rank[i][j] = min(rank[i][j], rank[i][k] + rank[k][j])

            # 플로이드 워셜 array 채우기
            if k == num_students:
                if rank[i][j] == INF and rank[j][i] != INF:
                    rank[i][j] = -(rank[j][i])

res = 0
for i in range(1, num_students + 1):
    count = num_students - (rank[i].count(INF) - 1)
    if count == num_students:
        res += 1

print(res)

# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4
# res = 1