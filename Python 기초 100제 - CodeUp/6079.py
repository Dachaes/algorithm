# 6079
x = int(input())
res = 0
for i in range(1, x):
    res += i
    if res >= x:
        print(i)
        break
