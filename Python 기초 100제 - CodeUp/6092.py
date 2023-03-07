# 6092
n = int(input())
m = list(map(int, input().split()))
num = [0 for i in range(23)]
for calling in m:
    num[calling - 1] += 1

for i in range(0, 23):
    print(num[i], end=' ')
