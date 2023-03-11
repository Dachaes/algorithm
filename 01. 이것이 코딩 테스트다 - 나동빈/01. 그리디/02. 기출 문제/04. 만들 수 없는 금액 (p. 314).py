# 04. 만들 수 없는 금액 (p. 314)

# Input
N = int(input())
coins = list(map(int, input().split()))
coins.sort()

price = 1
for coin in coins:
    if price >= coin:
        price += coin
    else:
        break

print(price)