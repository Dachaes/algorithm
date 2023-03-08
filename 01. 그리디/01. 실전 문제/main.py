# 02. 숫자 카드 게임 (p. 96)

# input
N, M = map(int, input().split())
num_cards = []
for _ in range(N):
    num_cards.append(list(map(int, input().split())))

min_values = []
for row in num_cards:
    min_values.append(min(row))
res = max(min_values)

print(res)
