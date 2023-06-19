# 29. 공유기 설치 (p. 369)
# https://www.acmicpc.net/problem/2110
import sys

# Input
n, c = map(int, sys.stdin.readline().split())               # n: 집의 개수, c: 공유기의 개수
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline()))
houses.sort()


def find_optimal_gap(start, end):
    gap = -1
    while start <= end:
        mid = (start + end) // 2
        num_routers = possible_routers(mid)
        if num_routers < c:
            end = mid - 1
        else:
            start = mid + 1
            gap = mid

    return gap


def possible_routers(gap):
    target = houses[0] + gap
    count = 1
    for house in houses:
        if house >= target:
            target = house + gap
            count += 1

    return count


min_gap, max_gap = 1, houses[-1] - houses[0]

if c == 2:
    answer = max_gap
else:
    answer = find_optimal_gap(min_gap, max_gap)

print(answer)