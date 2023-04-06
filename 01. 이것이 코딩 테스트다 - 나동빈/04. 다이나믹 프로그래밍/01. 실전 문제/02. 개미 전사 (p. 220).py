# 02. 개미 전사 (p. 220)

# Input
num_warehouse = int(input())
warehouses = list(map(int, input().split()))

sum_food = [warehouses[0], max(warehouses[0], warehouses[1])]
for i in range(2, num_warehouse):
    sum_food.append(max(sum_food[i - 2] + warehouses[i], sum_food[i - 1]))

res = sum_food[num_warehouse]
print(res)