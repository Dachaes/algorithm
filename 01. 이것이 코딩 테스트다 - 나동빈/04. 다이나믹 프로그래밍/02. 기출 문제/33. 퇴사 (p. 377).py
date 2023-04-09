# 33. 퇴사 (p. 377)
# https://www.acmicpc.net/problem/14501

# Input
date = int(input())
plan = [[0, 0]]
for i in range(date):
    plan.append(list(map(int, input().split())))

max_profit = [0] * (date + 2)

for i in range(date, 0, -1):
    if i + plan[i][0] <= date + 1:
        max_profit[i] = max(plan[i][1] + max_profit[i + plan[i][0]], max_profit[i + 1])
    else:
        max_profit[i] = max_profit[i + 1]

print(max_profit[1])