# 29. 공유기 설치 (p. 369)
# https://www.acmicpc.net/problem/2110
import sys

# Input
n, c = map(int, sys.stdin.readline().split())               # n: 집의 개수, c: 공유기의 개수
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline()))
houses.sort()

houses_with_router = []

def install_router(start, end):


    return


if c == 2:
    answer = n - 2
else:
    for i in range(1, c + 1):
        if i == 1:
            houses_with_router.append(houses[0])
        elif i == 2:
            houses_with_router.append(houses[-1])
        else:
            install_router()

print(answer)