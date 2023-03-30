# 26. 카드 정렬하기 (p. 363)
# https://www.acmicpc.net/problem/1715
import heapq

# Input
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))
heapq.heapify(cards)

res = 0
while len(cards) > 1:
    sum_cards = heapq.heappop(cards) + heapq.heappop(cards)
    cards.append(sum_cards)
    res += sum_cards

print(res)