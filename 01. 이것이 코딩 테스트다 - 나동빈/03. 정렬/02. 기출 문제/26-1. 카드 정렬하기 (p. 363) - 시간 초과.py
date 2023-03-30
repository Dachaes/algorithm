# 26. 카드 정렬하기 (p. 363)
# https://www.acmicpc.net/problem/1715

# Input
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

res = 0
while len(cards) > 1:
    cards.sort()

    sum_cards = cards.pop(1) + cards.pop(0)
    cards.append(sum_cards)
    res += sum_cards

print(res)