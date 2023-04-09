# 34. 병사 배치하기 (p. 380)
# https://www.acmicpc.net/problem/18353

# Input
num = int(input())
data = list(map(int, input().split()))
soldier = []
for i in range(1, num + 1):
    soldier.append([i, data[i - 1]])

index = 0
army, temp_army = [], []
while index != num - 1:
    if soldier[index][1] >= soldier[index + 1][1]:
        if temp_army:
            for temp in temp_army:
                army.append(temp)
            temp_army = []
        else:
            army.append(soldier[index])
    elif soldier[index][1] < soldier[index + 1][1]:
        temp_army.append(soldier[index + 1])

    index += 1
    if index == num - 1 and temp_army:
        for temp in temp_army:
            army.append(temp)
        temp_army = []

res = num - len(army)
print(res)