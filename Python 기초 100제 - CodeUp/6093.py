# 6093
n = int(input())
m = list(map(int, input().split()))
reverse_m = []
for i in range(n - 1, -1, -1):
    reverse_m.append(m[i])
for member in reverse_m:
    print(member)
