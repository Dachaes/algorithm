# 32. 정수 삼각형 (p. 376)
# https://www.acmicpc.net/problem/1932

# Input
size = int(input())
triangle = []
sum_number = []
for _ in range(size):
    data = list(map(int, input().split()))
    triangle.append(data)
    sum_number.append([0] * len(data))

sum_number[0][0] = triangle[0][0]
for i in range(1, size):
    for j in range(len(triangle[i])):
        left_up = [i - 1, j - 1]
        right_up = [i - 1, j]
        up = []
        if 0 <= j - 1 < len(triangle[i - 1]):
            up.append(sum_number[left_up[0]][left_up[1]])
        if 0 <= j < len(triangle[i - 1]):
            up.append(sum_number[right_up[0]][right_up[1]])
        sum_number[i][j] = triangle[i][j] + max(up)

res = max(sum_number[size - 1])
print(res)