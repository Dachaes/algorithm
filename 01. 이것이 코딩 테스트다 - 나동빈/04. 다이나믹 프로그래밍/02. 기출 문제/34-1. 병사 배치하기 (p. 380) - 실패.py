# 34. 병사 배치하기 (p. 380)
# https://www.acmicpc.net/problem/18353

# Input
num = int(input())
data = list(map(int, input().split()))
soldier = []
for i in range(1, num + 1):
    soldier.append([i, data[i - 1]])

print(soldier)
index = 0
army, temp_army = [], []
while index != num - 1:
    print(f"index: {index} // {soldier[index]} 과 {soldier[index + 1]}")
    if soldier[index][1] >= soldier[index + 1][1]:
        if temp_army:
            for temp in temp_army:
                army.append(temp)
            temp_army = []
        else:
            army.append(soldier[index])
        print(f"-> check1 // army: {army}, temp_army: {temp_army}")
    elif soldier[index][1] < soldier[index + 1][1]:
        temp_army.append(soldier[index + 1])
        print(f"-> check2 // army: {army}, temp_army: {temp_army}")

    index += 1
    if index == num - 1 and temp_army:
        for temp in temp_army:
            army.append(temp)
        temp_army = []
        print(f"-> check3 // army: {army}, temp_army: {temp_army}")

res = num - len(army)

print(res)