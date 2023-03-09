# 02. 곱하기 혹은 더하기 (p. 312)

# input
number = list(map(int, input()))

res = number[0]
for i in range(1, len(number)):
    if number[i] == 0:
        continue
    elif res == 0 or number[i] == 1:
        res += number[i]
    else:
        res *= number[i]

print(res)