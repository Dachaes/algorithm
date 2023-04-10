# 34. 병사 배치하기 (p. 380)
# https://www.acmicpc.net/problem/18353
# 코드를 돌리면 정답은 나오지만, 메모리 초과

# Input
num = int(input())
data = list(map(int, input().split()))
soldier = [[0, 0]]
for i in range(1, num + 1):
    soldier.append([i, data[i - 1]])

armys = [[soldier[1][0]]]
max_size = 0
for i in range(2, num + 1):
    new_army = 1
    #print(f"** armys: {armys}")
    for army in armys:
        #print(f" army: {army} // 차례: {i}- {soldier[i][1]}")
        if soldier[army[-1]][1] > soldier[i][1]:
            #print("  check1")
            army.append(i)
            new_army = 0
        elif soldier[army[0]][1] > soldier[i][1] > soldier[i - 1][1] and (i - 1) in army:
            #print("  check2")
            temp = []
            for index in army:
                temp.append(index)
            temp.pop(-1)
            temp.append(i)
            armys.append(temp)
            new_army = 0
    if new_army and i < (num + 1) // 2:
        #print("  check3")
        armys.append([i])

#print(f"** armys: {armys}")
final_army = 0
for army in armys:
    if final_army < len(army):
        final_army = len(army)
print(num - final_army)