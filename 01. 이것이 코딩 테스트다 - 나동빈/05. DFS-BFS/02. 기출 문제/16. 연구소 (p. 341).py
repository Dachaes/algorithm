# 16. 연구소 (p. 341)
# https://www.acmicpc.net/problem/14502
from collections import deque
import sys

# Input
n, m = map(int, sys.stdin.readline().split())
lab = []

for _ in range(n):
    lab_data = list(map(int, sys.stdin.readline().split()))
    lab.append(lab_data)

safety_zone = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 원본의 연구실을 복제하여 새 연구실 생성하는 함수
def replicate(origin):
    replica = [row.copy() for row in origin]
    return replica


# 복제한 연구실을 오염시키는 함수
def contaminate(x, y):
    for k in range(4):
        new_x, new_y = x + dx[k], y + dy[k]
        if (0 <= new_x < n and 0 <= new_y < m) and new_lab[new_x][new_y] == 0:
            new_lab[new_x][new_y] = 2
            contaminate(new_x, new_y)

# 복제한 연구실이 잘 오염되었는지 확인하는 함수
def print_lab(place):
    for i in range(n):
        for j in range(m):
            print(place[i][j], end=" ")
        print("")


new_lab = replicate(lab)
new_safety_zone = 0
for i in range(n):
    for j in range(m):
        if new_lab[i][j] == 2:
            contaminate(i, j)
        elif new_lab[i][j] == 0:
            new_safety_zone += 1
# print_lab(new_lab)
safety_zone = max(safety_zone, new_safety_zone)
# print(safety_zone)