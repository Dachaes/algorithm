# 04. 효율적인 화폐 구성 (p. 226)

# Input
num, target = map(int, input().split())
moneys = []
for _ in range(num):
    moneys.append(int(input()))
moneys.sort()

sum_price = [0]
for i in range(1, target + 1):
    # 1. 목표값이 가지고 있는 화폐의 단위보다 작을 경우, 불가능 -> -1
    if i < moneys[0]:
        sum_price.append(-1)
    # 2. 목표값이 가지고 있는 화폐의 단위랑 동일할 경우, 화폐 단위 한개로 만들 수 있음 -> 1
    elif i in moneys:
        sum_price.append(1)
    # 3. 목표값이 가지고 있는 화폐의 합으로 계산해야 할 경우,
    # 이전에 계산했던 값(이전 누적값) + 가지고 있는 화폐 단위(1개)로 계산이 가능한지 확인
    else:
        temp = -1
        for money in moneys:
            if i - money > 0 and sum_price[i - money] != -1:
                if temp == -1:
                    temp = sum_price[i - money] + 1
                else:
                    temp = min(temp, sum_price[i - money] + 1)
        sum_price.append(temp)

print(sum_price[target])