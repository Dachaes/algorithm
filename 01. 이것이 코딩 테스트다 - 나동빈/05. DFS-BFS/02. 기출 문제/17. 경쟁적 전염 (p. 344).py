# 17. 경쟁적 전염 (p. 344)
# https://www.acmicpc.net/problem/18405
import sys

# Input
n, k = map(int, sys.stdin.readline().split())
test_tube = []
incontaminated = 0
for _ in range(n):
    tube_data = list(map(int, sys.stdin.readline().split()))
    incontaminated += tube_data.count(0)
    test_tube.append(tube_data)
s, x, y = map(int, sys.stdin.readline().split())
x, y = x - 1, y - 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while incontaminated != 0:
