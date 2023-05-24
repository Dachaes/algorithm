# 17. 경쟁적 전염 (p. 344)
# https://www.acmicpc.net/problem/18405
import sys
from collections import deque

# Input
n, k = map(int, sys.stdin.readline().split())
test_tube = []                              # test_tube : 입력받은 시험관
list_tube = [[] for _ in range(k)]          # list_tube : 바이러스 종류에 따라 시험관의 위치 저장
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        virus_type = data[j]
        if virus_type != 0:
            list_tube[virus_type - 1].append([i, j])
    test_tube.append(data)
deq_tube = deque(list_tube)                 # deq_tube : list_tube를 deque화

s, target_x, target_y = map(int, sys.stdin.readline().split())
target_x, target_y = target_x - 1, target_y - 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 시험관을 전염시키는 함수
def contaminate(x, y, virus):
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if (0 <= new_x < n and 0 <= new_y < n) and test_tube[new_x][new_y] == 0:
            test_tube[new_x][new_y] = virus
            next_positions.append([new_x, new_y])


# 종료 1. 시간 s가 지나면 while 문을 더 이상 실행하지 않는다.
while s != 0:
    # 종료 2. 더 이상 전염시킬 수 없으면 while 문을 빠져 나온다.
    if not deq_tube:
        break
    # 종료 3. 타겟 위치에 이미 바이러스가 존재한다면 while 문을 빠져 나온다.
    if test_tube[target_x][target_y] != 0:
        break

    # 가지고 있는 바이러스 정보만큼 for 문을 돈다. (1 for 문 = 1초)
    for i in range(len(deq_tube)):
        positions_of_virus = deq_tube.popleft()
        next_positions = []
        for position in positions_of_virus:
            contaminate(position[0], position[1], i + 1)
        deq_tube.append(next_positions)
    s -= 1

print(test_tube[target_x][target_y])