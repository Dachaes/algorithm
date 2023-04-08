# 33. 퇴사 (p. 377)
# https://www.acmicpc.net/problem/14501

# Input
date = int(input())
plan = [[0, 0]]
for i in range(date):
    plan.append(list(map(int, input().split())))

print(plan)
for i in range(1, date + 1):
    for j in range(1, i + 1):
