# 6086
x = int(input())
res = 0
for i in range(1, x + 1):
    res += i
    if res >= x:
        print(res)
        break
