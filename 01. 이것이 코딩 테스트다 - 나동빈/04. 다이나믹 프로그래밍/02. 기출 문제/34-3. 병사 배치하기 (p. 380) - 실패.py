# 34. 병사 배치하기 (p. 380)
# https://www.acmicpc.net/problem/18353
# 34-2 코드의 리스트 저장방식을 단순화했으나, 19번째 줄에서 같은 전투력의 병사가 나올 경우가 문제
# 같은 전투력의 병사는 같은 군대 내에 있을 수 없다.

# Input
num = int(input())
data = list(map(int, input().split()))
soldier = [[0, 0]]
for i in range(1, num + 1):
    soldier.append([i, data[i - 1]])

armys = [[1, soldier[1][0], soldier[1][0]]]             # [인원 수, 최댓값의 병사 번호, 최솟값의 병사 번호
for i in range(2, num + 1):
    new_army = 1
    print(f"** armys: {armys}")
    for army in armys:
        print(f" army: {army} // 차례: {i}- {soldier[i][1]}")
        if soldier[army[1]][1] > soldier[i][1] > soldier[army[2]][1] and army[2] - army[1] != army[0] - 1:
            print("  check1")
            armys.append([army[0] + 1, army[1], army[2]])
            new_army = 0
        elif soldier[army[2]][1] > soldier[i][1]:
            print("  check2")
            army[0] += 1
            army[2] = soldier[i][0]
            new_army = 0
    if new_army:
        print("  check3")
        armys.append([1, soldier[i][0], soldier[i][0]])

print(f"** armys: {armys}")
max_soldiers = 0
for army in armys:
    if max_soldiers < army[0]:
        max_soldiers = army[0]
print(num - max_soldiers)