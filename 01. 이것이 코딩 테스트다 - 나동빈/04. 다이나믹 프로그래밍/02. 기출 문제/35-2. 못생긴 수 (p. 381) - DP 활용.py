# 35. 못생긴 수 (p. 381)

# Input
n = int(input())
ugly_numbers = [1]

indexs = [0, 0, 0]
numbers = [2, 3, 5]
for i in range(1, n):
    ugly_numbers.append(min(numbers))
    if ugly_numbers[i] == numbers[0]:
        indexs[0] += 1
        numbers[0] = ugly_numbers[indexs[0]] * 2
    if ugly_numbers[i] == numbers[1]:
        indexs[1] += 1
        numbers[1] = ugly_numbers[indexs[1]] * 3
    if ugly_numbers[i] == numbers[2]:
        indexs[2] += 1
        numbers[2] = ugly_numbers[indexs[2]] * 5

print(ugly_numbers[n - 1])