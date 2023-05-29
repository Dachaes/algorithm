# 21. 인구 이동 (p. 353)
# https://www.acmicpc.net/problem/16234
from collections import deque

# Input
n, min_diff, max_diff = map(int, input().split())
population = []
for _ in range(n):
    population.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_union(x, y, union_num):
    global union
    if union[x][y] == 0:
        print(f"({x}, {y}) 확인 중~")
        union[x][y] = union_num
        print(f"union: {union}")
        sum_people = population[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # print(f"  {i} -> ({nx}, {ny}) 들어 옴~")
                diff = abs(population[x][y] - population[nx][ny])
                if min_diff <= diff <= max_diff:
                    sum_people += population[nx][ny]
                    # print(f"--------------------------------")
                    check_union(nx, ny, union_num)
                    union_population.append(sum_people)
                else:
                    check_union(nx, ny, union_num + 1)


day = 1
union = [[0 for _ in range(n)] for _ in range(n)]
union_population = [0]
check_union(0, 0, 1)
print(f"union: {union}")
print(f"union_population: {union_population}")
