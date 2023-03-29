# 24. 안테나 (p. 360)
# https://www.acmicpc.net/problem/18310

# Input
num = int(input())
houses = list(map(int, input().split()))
houses.sort()

cnt = 0
res = [-1, 0]                   # [위치, 합]
sum_house = sum(houses)
for house in houses:
    distance = sum_house - (house * (num - cnt)) + (house * cnt)
    if res[0] == -1 or distance < res[1]:
        res[0] = house
        res[1] = distance
    sum_house -= (house * 2)
    cnt += 1

print(res[0])