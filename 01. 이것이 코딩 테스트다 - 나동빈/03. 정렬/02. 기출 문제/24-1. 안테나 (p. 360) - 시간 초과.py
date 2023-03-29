# 24. 안테나 (p. 360)
# https://www.acmicpc.net/problem/18310

# Input
num = int(input())
houses = list(map(int, input().split()))
houses.sort()

max_house = max(houses)
antenna = [-1] * (max_house + 1)
for pos in range(1, max_house + 1):
    distance = 0
    if pos in houses:
        for house in houses:
            distance += abs(house - pos)
        antenna[pos] = distance

res = -1
for i in range(1, max_house + 1):
    if antenna[i] != -1:
        if res == -1:
            res = i
        elif antenna[i] < antenna[res]:
            res = i

print(res)