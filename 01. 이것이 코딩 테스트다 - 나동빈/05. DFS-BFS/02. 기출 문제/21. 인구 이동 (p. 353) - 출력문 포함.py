# 21. 인구 이동 (p. 353)
# https://www.acmicpc.net/problem/16234
import sys

# Input
n, min_diff, max_diff = map(int, input().split())
nation = []
for _ in range(n):
    nation.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 모든 국가의 연합의 번호를 매기는 함수
def check_union(x, y, union_num):
    global union, num_of_nation, sum_of_population
    if union[x][y] == 0:
        union[x][y] = union_num
        sum_of_population += nation[x][y]
        num_of_nation += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                diff = abs(nation[x][y] - nation[nx][ny])
                if min_diff <= diff <= max_diff:
                    check_union(nx, ny, union_num)


day = 0
while True:
    # 1. 인구 이동을 할 수 있는 국가끼리 같은 연합 번호를 매긴다.
    union = [[0 for _ in range(n)] for _ in range(n)]   # union : 연합 번호 리스트
    union_number = 1                                    # union_number : 연합 번호
    union_average_population = [0]                      # union_average_population : 각 연합의 총 인구 수 / 각 연합의 국가 수
    for i in range(n):
        for j in range(n):
            if union[i][j] == 0:
                sum_of_population = 0                   # sum_of_population : 각 연합의 총 인구 수
                num_of_nation = 0                       # num_of_nation : 각 연합의 국가 수
                check_union(i, j, union_number)
                union_average_population.append(sum_of_population // num_of_nation)
                union_number += 1
    print(f"최종 union: {union}")
    print(f"최종 union_population: {union_average_population}")
    print(f"인구 이동 전: {nation}")

    # 종료 조건 : 모든 국가가 다른 연합에 속해 있으면(인구 이동이 불가능하면) while 문을 종료한다.
    # 종료 조건에 맞지 않으면 날짜를 증가하고, 인구 이동을 시작한다.
    max_union_number = union_number - 1                 # max_union_number : 현재 가장 큰 연합 번호
    if max_union_number == n * n:
        break
    else:
        day += 1

    # 2. 같은 연합 번호의 국가끼리 인구 이동을 한다.
    for i in range(n):
        for j in range(n):
            check_union_number = union[i][j]
            nation[i][j] = union_average_population[check_union_number]
    print(f"인구 이동 후: {nation}")
    print(f"-----인구 이동 한 직후 day: {day}-----")

print(day)