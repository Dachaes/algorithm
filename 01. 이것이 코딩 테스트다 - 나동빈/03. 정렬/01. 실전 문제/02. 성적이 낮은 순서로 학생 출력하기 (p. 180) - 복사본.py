# 01. 위에서 아래로 (p. 178)

# Input
num = int(input())
num_list = []
for _ in range(num):
    num_list.append(int(input()))

num_list.sort(reverse=True)

for i in range(num):
    print(num_list[i], end=" ")