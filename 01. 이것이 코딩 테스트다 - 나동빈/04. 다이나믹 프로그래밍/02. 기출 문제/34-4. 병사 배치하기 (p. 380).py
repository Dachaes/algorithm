# 34. 병사 배치하기 (p. 380)
# https://www.acmicpc.net/problem/18353

# Input
num = int(input())
data = list(map(int, input().split()))
soldier = []
for i in range(num):
    soldier.append(data[i])

army = [0] * num

for i in range(0, num):
    army[i] = 1
    for j in range(0, i):
        if soldier[j] > soldier[i]:
            army[i] = max(army[i], army[j] + 1)

res = num - max(army)
print(res)