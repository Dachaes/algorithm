# 16. 연구소 (p. 341)
# https://www.acmicpc.net/problem/14502
import sys
from itertools import combinations

# Input
n, m = map(int, sys.stdin.readline().split())
lab = []
for _ in range(n):
    lab_data = list(map(int, sys.stdin.readline().split()))
    lab.append(lab_data)

empty_space = []
cnt_empty = 0
safety_zone = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 원본의 연구실에서 빈 공간(0)의 위치를 empty_space 리스트에 저장하는 함수
def find_empty_space():
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                empty_space.append([i, j])


# 원본의 연구실을 복제하여 새 연구실 생성하는 함수
def replicate(origin, num):
    new_wall = possible_comb[num]
    replica = []
    for i in range(n):
        temp = []
        for j in range(m):
            set_up_new_wall = 0
            for k in range(3):
                if new_wall[k][0] == i and new_wall[k][1] == j:
                    set_up_new_wall = 1
            if set_up_new_wall:
                temp.append(1)
            else:
                temp.append(origin[i][j])
        replica.append(temp)
    return replica


# 복제한 연구실을 오염시키는 함수
def contaminate(x, y):
    for k in range(4):
        new_x, new_y = x + dx[k], y + dy[k]
        if (0 <= new_x < n and 0 <= new_y < m) and new_lab[new_x][new_y] == 0:
            new_lab[new_x][new_y] = 2
            contaminate(new_x, new_y)


find_empty_space()
# empty_space의 조합을 가져온다. (벽을 3개 세울 수 있는 모든 경우의 수)
possible_comb = list(combinations(empty_space, 3))
num_comb = len(possible_comb)

# 모든 경우의 수를 체크한다.
cnt = 0
while num_comb != cnt:
    # 1. 기존 연구실을 새 연구실에 복사한다.
    # while 문을 돌며 매번 복사할 때, 새 벽 3개를 세우는 작업도 함께 한다.
    new_lab = replicate(lab, cnt)
    new_safety_zone = 0

    # 2. 새로 만든 연구실의 오염을 진행시킨다.
    for i in range(n):
        for j in range(m):
            if new_lab[i][j] == 2:
                contaminate(i, j)

    # 3. 오염이 끝난 후에 안전한 공간(0)을 확인한다.
    for i in range(n):
        for j in range(m):
            if new_lab[i][j] == 0:
                new_safety_zone += 1

    safety_zone = max(safety_zone, new_safety_zone)
    cnt += 1
print(safety_zone)